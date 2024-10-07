import uuid
from datetime import datetime, timezone
from unittest import TestCase
from unittest.async_case import IsolatedAsyncioTestCase

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.sql_alchemy.repositories.products_repository import SqlAlchemyProductsRepository, Base
from app.adapters.sql_alchemy.session import get_session
from app.domain.model.product import Product

class TestSqlAlchemyProductsRepository(IsolatedAsyncioTestCase):
    async def test_add(self):
        print("init test_add")
        session = await get_session()


        # result = await session.execute(text("select 1"))
        print("create table  product")
        # current_time = datetime.now(timezone.utc).isoformat()
        # _id = str(uuid.uuid4())
        #
        # product_obj = Product(
        #     id=_id,
        #     name="Product test",
        #     description="Product",
        #     createDate=current_time,
        #     lastUpdateDate=current_time,
        # )
        # created_repository = SqlAlchemyProductsRepository(session=get_session())
        #
        # result = await created_repository.add(product=product_obj)
        #
        # assert product_obj.id is None
