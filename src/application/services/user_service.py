import email_validator
from pydantic import EmailStr

from src.application.domain.user import UserDto, UserRegistration, UserLogin, UserResponse
from src.exceptions import InvalidCredentialsException, InvalidPasswordException
from src.infrastructure.database.models import User
from src.infrastructure.database.repositories.user_repository import UserRepository
from src.infrastructure.utils.hash_service import HashService
from src.infrastructure.utils.token_service import TokenService


class UserService:

    @staticmethod
    async def create_user(user_data: UserRegistration) -> UserResponse:

        user_dto = UserDto(
            phone_number=user_data.phone_number,
            email=user_data.email,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            password_hash=HashService.hash(user_data.password))

        user: User = await UserRepository.create_user(user_dto)

        user_dto = UserDto(
            id=str(user.id),
            email=user.email,
            phone_number=user.phone_number,
            first_name=user.first_name,
            last_name=user.last_name,
            access_level=user.access_level)

        access_token = await TokenService.create_access_token(user_dto)

        return UserResponse(user_data=user_dto, access_token=access_token)

    @staticmethod
    async def login(user_data: UserLogin) -> UserResponse:

        if email_validator.validate_email(user_data.login):
            user: User = await UserRepository.get_user_by_email(user_data.login)
        else:
            user: User = await UserRepository.get_user_by_phone_number(user_data.login)

        if not user:
            raise InvalidCredentialsException

        if not HashService.verify(user.password_hash, user_data.password):
            raise InvalidPasswordException

        user_dto = UserDto(
            id=str(user.id),
            phone_number=user.phone_number,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            access_level=user.access_level)

        access_token = await TokenService.create_access_token(user=user_dto)

        return UserResponse(user_data=user_dto, access_token=access_token)
