from uuid import UUID

from sqlalchemy import select, update
from sqlalchemy.exc import SQLAlchemyError
from src.application.domain.category import CategoryCreate
from src.config import settings
from src.exceptions import CategoryAlreadyExistsException, CategoryNotFoundException
from src.infrastructure.database.database import async_session_maker
from src.infrastructure.database.models import Category, Product


class CategoryRepository:

    @staticmethod
    async def create_category(category_data: CategoryCreate) -> Category:
        async with async_session_maker() as session:
            existing_category = await session.execute(select(Category).filter_by(name=category_data.name))
            if existing_category.scalars().first():
                raise CategoryAlreadyExistsException(name=category_data.name)
            category = Category(name=category_data.name, description=category_data.description)
            session.add(category)
            try:
                await session.commit()
            except SQLAlchemyError as e:
                await session.rollback()
                raise e
            return category

    @staticmethod
    async def get_all_categories():
        async with async_session_maker() as session:
            query = select(Category)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def get_products_by_category(category_id: UUID):
        async with async_session_maker() as session:
            query = select(Product).filter_by(category_id=category_id)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def delete_category(category_id: str):
        async with async_session_maker() as session:
            result = await session.execute(select(Category).filter_by(id=category_id))
            category = result.scalars().first()

            if not category:
                raise CategoryNotFoundException

            none_category_result = await session.execute(select(Category).filter_by(name=settings.NONE_CATEGORY_NAME))
            none_category = none_category_result.scalars().first()

            if not none_category:
                raise CategoryNotFoundException

            await session.execute(update(Product).where(Product.category_id == category.id).values(category_id=none_category.id))

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


