import typing
from abc import ABC, abstractmethod

from app.domain.model.product import Product


class ProductsRepository(ABC):
    @abstractmethod
    async def add(self, product: Product) -> None:
        ...

    @abstractmethod
    async def update_attributes(self, product_id: str, **kwargs) -> None:
        ...

    @abstractmethod
    def get(self, product_id: str) -> typing.Optional[Product]:
        ...

    @abstractmethod
    async def delete(self, product_id: str) -> None:
        ...