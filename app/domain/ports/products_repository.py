import typing
from abc import ABC, abstractmethod

from app.domain.model.product import Product


class ProductsRepository(ABC):
    @abstractmethod
    async def add(self, product: Product) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def update_attributes(self, product_id: str, **kwargs) -> None:
        raise NotImplementedError()

    @abstractmethod
    def get(self, product_id: str) -> typing.Optional[Product]:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, product_id: str) -> None:
        raise NotImplementedError()