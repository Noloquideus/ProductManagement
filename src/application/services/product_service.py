from src.application.domain.product import ProductCreate
from src.config import settings
from src.infrastructure.database.repositories.product_repository import ProductRepository


class ProductService:

    @staticmethod
    async def create_product(product_data: ProductCreate):
        return await ProductRepository.create_product(product_data)
