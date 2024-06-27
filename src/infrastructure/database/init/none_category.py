from sqlalchemy import select
from src.config import settings
from src.infrastructure.database.database import async_session_maker
from src.infrastructure.database.models import Category


async def create_none_category():
    async with async_session_maker() as session:
        existing_category = await session.execute(select(Category).filter_by(name=settings.NONE_CATEGORY_NAME))
        category = existing_category.scalars().first()
        if not category:
            new_category = Category(name=settings.NONE_CATEGORY_NAME, description='product without category')
            session.add(new_category)
            await session.commit()
