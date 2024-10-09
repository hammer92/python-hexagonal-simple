import typing
from abc import ABC, abstractmethod

class ProductsRepository(ABC):
    @abstractmethod
    async def add(self, product: dict) -> dict:
        raise NotImplementedError()

    @abstractmethod
    async def update_attributes(self, product_id: str, **kwargs) -> dict:
        raise NotImplementedError()

    @abstractmethod
    def get(self, product_id: str) -> dict:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, product_id: str) -> None:
        raise NotImplementedError()