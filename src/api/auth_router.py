from fastapi import APIRouter, status, Response
from src.application.domain.user import UserRegistration, UserDto, UserResponse
from src.application.services.user_service import UserService
from src.infrastructure.utils.token_service import TokenService

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

    user_dto = UserDto(
        id=str(user.id),
        email=user.email,
        phone_number=user.phone_number,
        first_name=user.first_name,
        last_name=user.last_name,
        access_level=user.access_level)

    access_token = await TokenService.create_access_token(user_dto)

    response.status_code = status.HTTP_201_CREATED
    response.set_cookie(key="access_token", value=access_token, httponly=True, samesite="strict", secure=True)
    return user_dto
