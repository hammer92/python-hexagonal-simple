from unittest import TestCase, mock

from assertpy import assertpy

from app.domain.ports.products_repository import ProductsRepository
from app.domain.services.command.create_product_command import CreateProductCommand
from app.domain.services.command.create_product_command_handler import handle_create_product_command



class Test(TestCase):
    async def test_handle_create_product_command(self):
        # Arrange
        mock_products_repository = mock.create_autospec(
            spec=ProductsRepository, instance=True
        )
        command = CreateProductCommand(
            name="Test Product",
            description="Test Description",
        )

        await handle_create_product_command(command= command, products_repository = mock_products_repository)

        # Assert
        product = mock_products_repository.add.call_args.args[0]

        assertpy.assert_that(product.name).is_equal_to("Test Product")
        assertpy.assert_that(product.description).is_equal_to("Test Description")



