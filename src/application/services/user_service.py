from src.application.domain.user import UserDto, UserRegistration
from src.infrastructure.database.models import User
from src.infrastructure.database.repositories.user_repository import UserRepository
from src.infrastructure.utils.hash_service import HashService


class UserService:

    @staticmethod
    async def create_user(user_data: UserRegistration) -> User:

        user_dto = UserDto(
            phone_number=user_data.phone_number,
            email=user_data.email,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            password_hash=HashService.hash(user_data.password))

        user = await UserRepository.create_user(user_dto)

        return user

    @staticmethod
    async def get_user_by_id(user_id: int) -> User:
        pass

    @staticmethod
    async def get_user_by_email(email: str) -> User:
        pass

    @staticmethod
    async def get_user_by_phone(phone: str) -> User:
        pass

