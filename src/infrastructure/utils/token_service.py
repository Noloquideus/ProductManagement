from datetime import datetime, timedelta, timezone
import jwt
from src.application.domain.user import UserDto
from src.config import settings


class TokenService:

    @staticmethod
    async def create_access_token(user: UserDto) -> str:
        expire_delta = timedelta(minutes=settings.ACCESS_TTL_MINUTES)
        payload = {
            "sub": user.id,
            "email": user.email,
            "phone": user.phone_number,
            "access_level": user.access_level,
            "iat": datetime.now(timezone.utc),
            "exp": datetime.now(timezone.utc) + expire_delta
        }
        token = jwt.encode(payload, settings.ACCESS_SECRET_KEY, algorithm=settings.ALGORITHM)
        return token
