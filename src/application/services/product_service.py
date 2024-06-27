from uuid import UUID
from src.application.domain.product import ProductCreate, ProductUpdate
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
