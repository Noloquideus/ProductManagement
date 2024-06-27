from typing import Optional
from src.application.domain.category import CategoryCreate
from src.infrastructure.database.models import Category
from src.infrastructure.database.repositories.category_repository import CategoryRepository


class CategoryService:

    @staticmethod
    async def create_category(category_data: CategoryCreate) -> Category:
        return await CategoryRepository.create_category(category_data=category_data)

    @staticmethod
    async def get_all_categories():
        return await CategoryRepository.get_all_categories()

    @staticmethod
    async def get_products_by_category(category_id: str):
        return await CategoryRepository.get_products_by_category(category_id=category_id)

    @staticmethod
    async def delete_category(category_id: str):
        return await CategoryRepository.delete_category(category_id=category_id)

    @staticmethod
    async def update_category(category_id: str, name: Optional[str] = None, description: Optional[str] = None) -> Optional[Category]:
        return await CategoryRepository.update_category(category_id, name, description)
