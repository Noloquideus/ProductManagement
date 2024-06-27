from pydantic import BaseModel, Field


class CategoryCreate(BaseModel):
    name: str = Field(
        title="Category name",
        description="Name of the category",
        example="Electronics")
    description: str = Field(
        title="Category description",
        description="Description of the category",
        example="Electronics products")
