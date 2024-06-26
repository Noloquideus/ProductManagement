from uuid import UUID

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from src.application.domain.user import UserDto
from src.exceptions import UserAlreadyExistsException
from src.infrastructure.database.database import async_session_maker
from src.infrastructure.database.models import User


class UserRepository:

    @staticmethod
    async def create_user(user_data: UserDto) -> User:
        async with async_session_maker() as session:
            try:
                user = User(
                    email=user_data.email,
                    phone_number=user_data.phone_number,
                    first_name=user_data.first_name,
                    last_name=user_data.last_name,
                    password_hash=user_data.password_hash)
                session.add(user)
                await session.commit()
                return user

            except IntegrityError:
                await session.rollback()
                raise UserAlreadyExistsException

    @staticmethod
    async def add_refresh_token(user_id: UUID, refresh_token: str) -> None:
        pass

    @staticmethod
    async def get_user_by_id(user_id: UUID) -> User:
        pass

    @staticmethod
    async def get_user_by_email(email: str) -> User:
        async with async_session_maker() as session:
            query = select(User).filter_by(email=email)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @staticmethod
    async def get_user_by_phone_number(phone_number: str) -> User:
        async with async_session_maker() as session:
            query = select(User).filter_by(phone_number=phone_number)
            result = await session.execute(query)
            return result.scalar_one_or_none()
