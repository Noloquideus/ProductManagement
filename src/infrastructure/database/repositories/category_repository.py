from sqlalchemy import select
from src.application.domain.category import CategoryCreate
from src.infrastructure.database.database import async_session_maker
from src.infrastructure.database.models import Category


class CategoryRepository:

    @staticmethod
    async def create_category(category_data: CategoryCreate) -> Category:
        async with async_session_maker() as session:
            category = Category(name=category_data.name, description=category_data.description)
            session.add(category)
            await session.commit()
            return category

    @staticmethod
    async def get_all_categories():
        async with async_session_maker() as session:
            query = select(Category)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def get_products_by_category(category_id: str):
        pass

    @staticmethod
    async def delete_category(category_id: str):
        async with async_session_maker() as session:
            result = await session.execute(select(Category).filter_by(id=category_id))
            category = result.scalars().first()
            if category:
                await session.delete(category)
                await session.commit()
            return category

    @staticmethod
    async def update_category(category_id: str, name: str = None, description: str = None):
        async with async_session_maker() as session:
            result = await session.execute(select(Category).filter_by(id=category_id))
            category = result.scalars().first()
            if category:
                if name is not None:
                    category.name = name
                if description is not None:
                    category.description = description
                await session.commit()
            return category


