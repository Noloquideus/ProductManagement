from uuid import UUID
from src.application.domain.user import UserDto
from src.infrastructure.database.models import User


class UserRepository:

    @staticmethod
    async def create_user(user_data: UserDto) -> User:
        pass

    @staticmethod
    async def add_refresh_token(user_id: UUID, refresh_token: str) -> None:
        pass

    @staticmethod
    async def get_user_by_id(user_id: UUID) -> User:
        pass

    @staticmethod
    async def get_user_by_email(email: str) -> User:
        pass

    @staticmethod
    async def get_user_by_phone_number(phone_number: str) -> User:
        pass

    @staticmethod
    async def delete_all_refresh_tokens(user_id: UUID) -> None:
        pass

    @staticmethod
    async def delete_refresh_token(user_id: UUID, refresh_token: str) -> None:
        pass
