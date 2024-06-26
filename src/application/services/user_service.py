from src.application.domain.user import UserDto
from src.infrastructure.database.models import User


class UserService:

    @staticmethod
    async def create_user(user_data: UserDto) -> User:
        pass

    @staticmethod
    async def get_user_by_id(user_id: int) -> User:
        pass

    @staticmethod
    async def get_user_by_email(email: str) -> User:
        pass

    @staticmethod
    async def get_user_by_phone(phone: str) -> User:
        pass

