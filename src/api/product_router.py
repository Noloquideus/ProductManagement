from typing import Optional, List
from uuid import UUID
from fastapi import APIRouter, status, Query, Cookie
from fastapi_cache.decorator import cache
from src.api.auth.decorator import require_min_access_level
from src.application.domain.product import ProductCreate, ProductUpdate, ProductResponse
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
@require_min_access_level(5)
async def create_product(product_data: ProductCreate, access_token: str = Cookie('access_token')):
    return await ProductService.create_product(product_data)


@product_router.get(
    path='/{product_id}',
    status_code=status.HTTP_200_OK,
    description='Get a product by ID',
    summary='Get a product by ID',
    response_description='The requested product')
@cache(expire=180)
async def get_product(product_id: UUID):
    product = await ProductService.get_product_by_id(product_id)
    return product


@product_router.get(
    path='/',
    status_code=status.HTTP_200_OK,
    description='Get products by filters',
    summary='Get products by filters',
    response_description='The requested products')
@cache(expire=180)
async def get_products(
    name: Optional[str] = Query(None, description="Filter by product name"),
    min_price: Optional[float] = Query(None, description="Filter by minimum price"),
    max_price: Optional[float] = Query(None, description="Filter by maximum price"),
    min_quantity: Optional[int] = Query(None, description="Filter by minimum quantity"),
    max_quantity: Optional[int] = Query(None, description="Filter by maximum quantity"),
    category_id: Optional[UUID] = Query(None, description="Filter by category ID")
) -> List[ProductResponse]:
    return await ProductService.get_products(name, min_price, max_price, min_quantity, max_quantity, category_id)


@product_router.put(path='/{product_id}')
@require_min_access_level(5)
async def update_product(product_data: ProductUpdate, access_token: str = Cookie('access_token')):
    return await ProductService.update_product(product_data)


@product_router.delete(path='/{product_id}')
@require_min_access_level(5)
async def delete_product(product_id: str, access_token: str = Cookie('access_token')):
    return await ProductService.delete_product(product_id=UUID(product_id))
