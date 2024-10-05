import uuid
from datetime import datetime, timezone

from app.domain.model.product import Product
from app.domain.ports.products_repository import ProductsRepository
from app.domain.services.command.create_product_command import CreateProductCommand


async def handle_create_product_command(command: CreateProductCommand,
                                  products_repository: ProductsRepository) -> str:
    current_time = datetime.now(timezone.utc).isoformat()
    _id = str(uuid.uuid4())

    product_obj = Product(
        id=_id,
        name=command.name,
        description=command.description,
        createDate=current_time,
        lastUpdateDate=current_time,
    )

    await products_repository.add(product_obj)

    return _id