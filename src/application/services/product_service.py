from src.application.domain.product import ProductCreate
from src.config import settings
from src.infrastructure.database.repositories.product_repository import ProductRepository


class ProductService:

    @staticmethod
    async def create_product(product_data: ProductCreate):
        if product_data.category_id is None:
            product_data.category_id = settings.NONE_CATEGORY_NAME
        return await ProductRepository.create_product(product_data)
