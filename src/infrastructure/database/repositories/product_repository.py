from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from src.application.domain.product import ProductCreate
from src.exceptions import ProductAlreadyExistsException
from src.infrastructure.database.database import async_session_maker
from src.infrastructure.database.models import Product


class ProductRepository:

    @staticmethod
    async def create_product(product_data: ProductCreate) -> Product:
        async with async_session_maker() as session:
            existing_product = await session.execute(select(Product).filter_by(name=product_data.name))
            if existing_product.scalars().first():
                raise ProductAlreadyExistsException

            product = Product(name=product_data.name, description=product_data.description, price=product_data.price)
            session.add(product)
            try:
                await session.commit()
            except SQLAlchemyError as e:
                await session.rollback()
                raise e
            return product