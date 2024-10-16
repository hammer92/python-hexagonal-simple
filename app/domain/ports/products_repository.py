import typing
from abc import ABC, abstractmethod

class ProductsQueryRepository(ABC):
    @abstractmethod
    async def get(self, product_id: str) -> typing.Optional[dict]:
        raise NotImplementedError()

    @abstractmethod
    async def list(self, **kwargs) -> typing.List[dict]:
        raise NotImplementedError()

class ProductsCommandRepository(ABC):
    @abstractmethod
    async def add(self, product: dict) -> dict:
        raise NotImplementedError()

    @abstractmethod
    async def update_attributes(self, product_id: str, **kwargs) -> dict:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, product_id: str) -> None:
        raise NotImplementedError()