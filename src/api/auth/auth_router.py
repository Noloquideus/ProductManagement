from fastapi import APIRouter, status, Response
from src.application.domain.user import UserRegistration, UserLogin
from src.application.services.user_service import UserService

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}, 500: {"description": "Internal server error"}, 400: {"description": "Bad request"}})


@auth_router.post(
    path='/register',
    status_code=status.HTTP_201_CREATED,
    description='Register a new user by providing an email, username, and password.',
    summary='Register a new user',
    response_description='The newly registered user without the password',
    responses={
        status.HTTP_201_CREATED: {"description": "User successfully created"},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid input data"},
        status.HTTP_409_CONFLICT: {"description": "User already exists"}})
async def register(response: Response, user_data: UserRegistration):
    user = await UserService.create_user(user_data)
    response.set_cookie(key="access_token", value=user.access_token, httponly=True, samesite="strict", secure=True)
    return user.user_data


@auth_router.post(
    path='/login',
    status_code=200,
    description='Login a user by providing an email and password. Returns the logged in user\'s information excluding the password.',
    summary='Login a user',
    response_description='User and access and refresh tokens',
    responses={
        200: {"description": "User successfully logged in"},
        400: {"description": "Invalid password"},
        401: {"description": "Invalid credentials"},
        500: {"description": "Internal server error"}})
async def login(response: Response, user_data: UserLogin):
    user = await UserService.login(user_data)
    response.set_cookie(key="access_token", value=user.access_token, httponly=True, samesite="strict", secure=True)
    return user.user_data
