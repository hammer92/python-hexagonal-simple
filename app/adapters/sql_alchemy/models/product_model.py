from typing import Optional

from sqlalchemy import String, UUID, Uuid
from sqlalchemy.orm import mapped_column, Mapped

from app.adapters.sql_alchemy.models.base_model import Base, TimestampMixin

class ProductModel(Base, TimestampMixin):
    __tablename__ = "products"

    id:  Mapped[UUID] = mapped_column(Uuid,primary_key=True)
    name:  Mapped[str] =  mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(String(3000))

def product_entity_to_model(product:dict) -> ProductModel:
    return ProductModel(
        id = product["id"],
        name = product["name"],
        description = product["description"]
    )

def product_model_to_entity(product:ProductModel) -> dict:
    return product.to_dict()

