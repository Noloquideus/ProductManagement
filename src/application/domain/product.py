from typing import Optional
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
    category_id: Optional[str] = Field(
        title="Product category",
        description="Category of the product",
        default=None)
