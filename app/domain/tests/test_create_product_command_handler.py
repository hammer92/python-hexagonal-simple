import uuid
from datetime import datetime, timezone
from unittest import TestCase, mock
from unittest.mock import AsyncMock, patch

import pytest
from assertpy import assertpy

from app.domain.model.product import Product
from app.domain.ports.products_repository import ProductsCommandRepository
from app.domain.services.command.create_product.command import CreateProductCommand
from app.domain.services.command.create_product.command_handler import handle_create_product_command



class TestCreateProduct(TestCase):
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


@pytest.mark.asyncio
async def test_handle_create_product_command():
    # Arrange
    mock_command = CreateProductCommand(name="Test Product", description="A test product")
    mock_repository = AsyncMock(spec=ProductsCommandRepository)
    mock_repository.add.return_value = None

    fixed_uuid = "12345678-1234-5678-1234-567812345678"
    fixed_time = datetime(2023, 1, 1, tzinfo=timezone.utc)

    # Act
    with patch('uuid.uuid4', return_value=uuid.UUID(fixed_uuid)), \
            patch('datetime.datetime', wraps=datetime) as mock_datetime:
        mock_datetime.now.return_value = fixed_time
        result = await handle_create_product_command(mock_command, mock_repository)

    # Assert
    assert result == fixed_uuid

    expected_product = Product(
        id=fixed_uuid,
        name="Test Product",
        description="A test product",
        createDate=fixed_time.isoformat(),
        lastUpdateDate=fixed_time.isoformat()
    )
    mock_repository.add.assert_called_once_with(expected_product.model_dump())

    assert mock_datetime.now.call_count == 1
    mock_datetime.now.assert_called_with(timezone.utc)

