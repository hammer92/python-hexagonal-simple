from datetime import datetime, timezone

from app.domain.ports.products_repository import ProductsCommandRepository
from app.domain.services.command.update_product.command import UpdateProductCommand


async def handle_update_product_command(command: UpdateProductCommand,
                                  products_repository: ProductsCommandRepository) -> str:
    current_time = datetime.now(timezone.utc).isoformat()

    attr_to_update = {
        "lastUpdateDate": current_time,
    }
    if command.name:
        attr_to_update["name"] = command.name
    if command.description:
        attr_to_update["description"] = command.description

    await products_repository.update_attributes(product_id=command.id, **attr_to_update)

    return command.id