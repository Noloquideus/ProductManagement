from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from src.application.domain.product import ProductCreate
from src.config import settings
from src.exceptions import ProductAlreadyExistsException, CategoryNotFoundException
from src.infrastructure.database.database import async_session_maker
from src.infrastructure.database.models import Product, Category


class ProductRepository:

    @staticmethod
    async def create_product(product_data: ProductCreate) -> Product:
        async with async_session_maker() as session:
            existing_product = await session.execute(select(Product).filter_by(name=product_data.name))
            if existing_product.scalars().first():
                raise ProductAlreadyExistsException

            product = Product(
                category_id=product_data.category_id,
                name=product_data.name,
                description=product_data.description,
                price=product_data.price,
                quantity=product_data.quantity)
            session.add(product)

            try:
                await session.commit()
            except SQLAlchemyError as e:
                await session.rollback()
                raise e

            return product
