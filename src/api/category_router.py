from uuid import UUID
from fastapi import APIRouter, status, Cookie
from fastapi_cache.decorator import cache
from src.api.auth.decorator import require_min_access_level
from src.application.domain.category import CategoryCreate
from src.application.services.category_service import CategoryService


category_router = APIRouter(
    prefix="/categories",
    tags=["categories"],
    responses={404: {"description": "Not found"}, 500: {"description": "Internal server error"}, 400: {"description": "Bad request"}})


@category_router.post(
    path='/',
    status_code=status.HTTP_201_CREATED,
    description='Create a new category',
    summary='Create a new category')
@require_min_access_level(5)
async def create_category(category_data: CategoryCreate, access_token: str = Cookie('access_token')):
    return await CategoryService.create_category(category_data=category_data)


@category_router.get(
    path='/',
    status_code=status.HTTP_200_OK,
    description='Get all categories',
    summary='Get all categories')
@cache(expire=300)
async def get_all_categories():
    return await CategoryService.get_all_categories()


@category_router.get(
    path='/{category_id}',
    status_code=210,
    description='Get products of category',
    summary='Get products of category by id')
@cache(expire=300)
async def get_products_by_category(category_id: UUID):
    return await CategoryService.get_products_by_category(category_id=category_id)


@category_router.delete(
    path='/{category_id}',
    status_code=status.HTTP_204_NO_CONTENT,
    description='Delete category by id',
    summary='Delete category by id')
@require_min_access_level(5)
async def delete_category(category_id: str, access_token: str = Cookie('access_token')):
    return await CategoryService.delete_category(category_id=category_id)


@category_router.put(
    path='/{category_id}',
    status_code=status.HTTP_200_OK,
    description='Update category by id',
    summary='Update category by id')
@require_min_access_level(5)
async def update_category(category_id: str, name: str, description: str, access_token: str = Cookie('access_token')):
    return await CategoryService.update_category(category_id=category_id, name=name, description=description)
