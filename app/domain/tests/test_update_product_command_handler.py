import logging
import uuid
from unittest import TestCase, mock

from assertpy import assertpy

from app.domain.ports.products_repository import ProductsRepository
from app.domain.services.command.update_product.command import UpdateProductCommand
from app.domain.services.command.update_product.command_handler import handle_update_product_command


class TestUpdateProduct(TestCase):
    async def test_handle_update_product_command(self):
        mock_products_repository = mock.create_autospec(
            spec=ProductsRepository, instance=True
        )

        # Update only the description
        product_id = str(uuid.uuid4())
        new_description = "New Description"
        command = UpdateProductCommand(
            id=product_id,
            description= new_description
        )

        # Act
        await handle_update_product_command(
            command=command, products_repository=mock_products_repository
        )

        # Assert

        updated_attributes = mock_products_repository.update_attributes.call_args.args

        assertpy.assert_that(updated_attributes["product_id"]).is_equal_to(product_id)
        assertpy.assert_that(updated_attributes["description"]).is_equal_to(new_description)

