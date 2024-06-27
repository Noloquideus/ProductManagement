import uuid
from sqlalchemy import Column, UUID, String, DateTime, func, Float, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY, INTEGER
from sqlalchemy.orm import relationship

from src.infrastructure.database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    phone_number = Column(String, nullable=False, unique=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    access_level = Column(INTEGER, nullable=False, default=1)
    date_created = Column(DateTime, nullable=False, default=func.now())


class Category(Base):
    __tablename__ = "categories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False, index=True)
    name = Column(String, nullable=False, unique=True, index=True)
    description = Column(String, nullable=True)
    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False, index=True)
    name = Column(String, nullable=False, index=True)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    quantity = Column(INTEGER, nullable=False)
    category_id = Column(UUID(as_uuid=True), ForeignKey('categories.id'), nullable=False)
    category = relationship("Category", back_populates="products")
