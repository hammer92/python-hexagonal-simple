import uuid

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.adapters.sql_alchemy.database_session_manager import DatabaseSessionManager
from app.adapters.sql_alchemy.models.base_model import Base
from app.adapters.sql_alchemy.models.product_model import product_entity_to_model, ProductModel, product_model_to_entity
from app.domain.ports.products_repository import ProductsRepository


class SqlAlchemyProductsRepository(ProductsRepository, DatabaseSessionManager):

    async def create_all(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    async def update_attributes(self, product_id: str, **kwargs) -> dict:
        pass

    async def get(self, product_id: uuid.UUID) -> dict:
        try:
            query = select(ProductModel).where(ProductModel.id == product_id)
            response = await self.session.execute(query)
            product_find = response.scalar_one_or_none()
            if product_find is None:
                raise Exception("Product not found")
            return product_model_to_entity(product_find)
        except IntegrityError:
            raise Exception("Error database")
        finally:
            await self.session.close()

    async def delete(self, product_id: str) -> None:
        pass

    async def add(self, product: dict) -> dict:
        instance = product_entity_to_model(product)
        try:
            async with self.session() as session:
                session.add(instance)
                await session.commit()
                await session.refresh(instance)
            return product_model_to_entity(instance)
        except IntegrityError:
            await self.session.rollback()
        finally:
            await self.session.close()


