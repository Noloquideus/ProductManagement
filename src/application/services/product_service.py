from typing import Optional, List
from uuid import UUID
from src.application.domain.product import ProductCreate, ProductUpdate, ProductResponse
from src.infrastructure.database.repositories.product_repository import ProductRepository


class ProductService:

    @staticmethod
    async def create_product(product_data: ProductCreate):
        return await ProductRepository.create_product(product_data)

    @staticmethod
    async def delete_product(product_id: UUID):
        return await ProductRepository.delete_product(product_id)

    @staticmethod
    async def update_product(product_data: ProductUpdate):
        return await ProductRepository.update_product(product_data)

    @staticmethod
    async def get_product_by_id(product_id: UUID) -> Optional[ProductResponse]:
        return await ProductRepository.get_product_by_id(product_id)

    @staticmethod
    async def get_products(
        name: Optional[str],
        min_price: Optional[float],
        max_price: Optional[float],
        min_quantity: Optional[int],
        max_quantity: Optional[int],
        category_id: Optional[UUID]
    ) -> List[ProductResponse]:
        return await ProductRepository.get_products(name, min_price, max_price, min_quantity, max_quantity, category_id)
