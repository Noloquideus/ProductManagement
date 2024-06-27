from fastapi import APIRouter, status
from src.application.domain.product import ProductCreate
from src.application.services.product_service import ProductService

product_router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Not found"}, 500: {"description": "Internal server error"}, 400: {"description": "Bad request"}})


@product_router.post(
    path='/',
    status_code=status.HTTP_201_CREATED,
    description='Create a new product',
    summary='Create a new product',
    response_description='The newly created product')
async def create_product(product_data: ProductCreate):
    return await ProductService.create_product(product_data)


@product_router.get(
    path='/{product_id}',
    status_code=status.HTTP_200_OK,
    description='Get a product by ID',
    summary='Get a product by ID',
    response_description='The requested product')
async def read_product():
    pass


@product_router.put(path='/{product_id}')
async def update_product():
    pass


@product_router.delete('/{product_id}')
async def delete_product():
    pass


# Здесь можно будет добавить эндпоинты с фильтрацией
@product_router.get('/filter')
async def filter_products():
    pass
