import uuid
import logging
from unittest.async_case import IsolatedAsyncioTestCase

from app.adapters.sql_alchemy.repositories.products_repository import SqlAlchemyProductsRepository
from app.domain.model.product import Product

_id = str("b35ef433-351d-4352-b908-3ff5c5675f1a")

class TestSqlAlchemyProductsRepository(IsolatedAsyncioTestCase):

    def setUp(self):
        self.logger = logging.getLogger(__name__)
        self.orig_handlers = self.logger.handlers
        self.logger.handlers = []
        self.level = self.logger.level

    async def test_add(self):
        # Arrange
        product_obj = Product(
            id=_id,
            name="Product test",
            description="Product"
        )
        created_repository = SqlAlchemyProductsRepository()
        await  created_repository.create_all()

        # Act
        result = await created_repository.add(product=product_obj.__dict__)

        # Assert
        assert result["created_at"] is not None
        self.assertEqual(result["id"], uuid.UUID(_id))

    async def test_get(self):
        self.logger.error('Started test_get')
        # Arrange
        created_repository = SqlAlchemyProductsRepository()

        # Act
        result = await created_repository.get(product_id=uuid.UUID(_id))

        # Assert
        self.logger.info("")
        assert result["created_at"] is not None
        self.assertEqual(result["id"], uuid.UUID(_id))
