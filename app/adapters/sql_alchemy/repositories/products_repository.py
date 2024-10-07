import typing
from datetime import datetime

from sqlalchemy import Column, String, TIMESTAMP, UUID, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import  DeclarativeBase, mapped_column, Mapped
from sqlalchemy.sql.annotation import Annotated
from sqlalchemy.sql.functions import now

from app.domain.model.product import Product
from app.domain.ports.products_repository import ProductsRepository


STR255 = Annotated[str, mapped_column(String(255))]
UniqueIdentifier = UUID(as_uuid=True)
class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=now())
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=now(), onupdate=now())

class Base(DeclarativeBase):...

class ProductModel(Base, TimestampMixin):

    __tablename__ = "products"

    id: str = Column(UniqueIdentifier,
                        ForeignKey("listing.id"),
                        primary_key=True)
    name: str =  Mapped[STR255]
    description: Mapped[typing.Optional[str]] = mapped_column(String(3000))


def product_entity_to_model(product:Product) -> ProductModel:
    return ProductModel(
        id = product.id,
        name = product.name,
        description = product.description,
        created_at = product.createDate,
        updated_at = product.lastUpdateDate
    )


class SqlAlchemyProductsRepository(ProductsRepository):

    def __init__(self, session: AsyncSession, identity_map=None):
        self.session = session
        self._identity_map = identity_map or dict()

    async def update_attributes(self, product_id: str, **kwargs) -> None:
        pass

    def get(self, product_id: str) -> typing.Optional[Product]:
        pass

    async def delete(self, product_id: str) -> None:
        pass

    # noinspection PyUnresolvedReferences
    async def add(self, product: Product) -> ProductModel:
        self._identity_map[product.id] = product
        instance = product_entity_to_model(product)
        try:
            self.session.add(instance)
            await self.session.commit()
            await self.session.refresh(instance)
            return instance
        except IntegrityError:
            await session.rollback()
            raise HTTPException(
                status_code=409,
                detail="User already exists",
            )

