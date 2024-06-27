from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.api.auth.auth_router import auth_router
from src.api.category_router import category_router
from src.api.product_router import product_router
from src.infrastructure.database.init.none_category import create_none_category
from src.infrastructure.database.init.redis import init_redis
from src.infrastructure.database.init.superadmin import create_superadmin


@asynccontextmanager
async def lifespan(_):
    await init_redis()
    await create_superadmin()
    await create_none_category()
    print("startup")
    yield
    print("shutdown")


app = FastAPI(title='Auth Service', description='Auth Service API', version='1.0.0', redoc_url=None, lifespan=lifespan)
app.include_router(auth_router)
app.include_router(category_router)
app.include_router(product_router)


@app.get("/")
async def root():
    return {"message": "Auth service"}
