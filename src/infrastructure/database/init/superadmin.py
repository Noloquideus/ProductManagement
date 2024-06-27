from src.config import settings
from src.infrastructure.database.database import async_session_maker
from src.infrastructure.database.models import User
from src.infrastructure.utils.hash_service import HashService


async def create_superadmin():
    async with async_session_maker() as session:
        superadmin = User(
            email=settings.SUPERADMIN_EMAIL,
            phone_number=settings.SUPERADMIN_PHONE,
            first_name=settings.SUPERADMIN_FIRSTNAME,
            last_name=settings.SUPERADMIN_LASTNAME,
            password_hash=HashService.hash(settings.SUPERADMIN_PASSWORD),
            access_level=settings.SUPERADMIN_ACCESS_LEVEL)
        session.add(superadmin)
        await session.commit()

