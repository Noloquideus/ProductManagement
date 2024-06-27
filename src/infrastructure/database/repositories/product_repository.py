from uuid import UUID

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from src.application.domain.product import ProductCreate, ProductUpdate
from src.exceptions import ProductAlreadyExistsException, ProductNotFoundException, CategoryNotFoundException
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

    @staticmethod
    async def delete_product(product_id: UUID):
        async with async_session_maker() as session:
            result = await session.execute(select(Product).filter_by(id=product_id))
            product = result.scalars().first()
            if not product:
                raise ProductNotFoundException
            await session.delete(product)
            await session.commit()
            return product

    @staticmethod
    async def update_product(product_data: ProductUpdate):
        async with async_session_maker() as session:

            result = await session.execute(select(Product).filter_by(id=product_data.product_id))
            product = result.scalars().first()

            if not product:
                raise ProductNotFoundException

            if product_data.name is not None:
                product.name = product_data.name
            if product_data.description is not None:
                product.description = product_data.description
            if product_data.price is not None:
                product.price = product_data.price
            if product_data.quantity is not None:
                product.quantity = product_data.quantity
            if product_data.category_id is not None:
                result = await session.execute(select(Category).filter_by(id=product_data.category_id))
                category = result.scalars().first()
                if not category:
                    raise CategoryNotFoundException

                product.category_id = category.id

            try:
                await session.commit()
            except SQLAlchemyError as e:
                await session.rollback()
                raise e

            return product
