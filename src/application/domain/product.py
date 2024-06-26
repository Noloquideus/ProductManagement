from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str = Field(
        title="Product name",
        description="Name of the product",
        min_length=1,
        max_length=100,
        examples=["Product 1", "Product 2"])
    description: str = Field(
        title="Product description",
        description="Description of the product",
        min_length=1,
        max_length=100,
        examples=["This is a product", "This is another product"])
    price: float = Field(
        title="Product price",
        description="Price of the product",
        ge=0,
        examples=[100.0, 200.0])
    quantity: int = Field(
        title="Product quantity",
        description="Quantity of the product",
        ge=0,
        examples=[10, 20])
    category_id: Optional[UUID] = Field(
        title="Product category id",
        description="Category of the product")


class ProductUpdate(BaseModel):
    product_id: UUID = Field(
        title="Product id",
        description="Id of the product")
    name: Optional[str] = Field(
        title="Product name",
        description="Name of the product",
        min_length=1,
        max_length=100)
    description: Optional[str] = Field(
        title="Product description",
        description="Description of the product",
        min_length=1,
        max_length=100)
    price: Optional[float] = Field(
        title="Product price",
        description="Price of the product",
        ge=0)
    quantity: Optional[int] = Field(
        title="Product quantity",
        description="Quantity of the product",
        ge=0)
    category_id: Optional[UUID] = Field(
        title="Product category id",
        description="Change category")


class ProductResponse(BaseModel):
    id: UUID
    name: str
    description: str
    price: float
    quantity: int
    category_id: UUID

    class Config:
        from_attributes = True
