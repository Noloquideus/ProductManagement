from datetime import datetime, timedelta, timezone
from typing import Dict
import jwt
from src.application.domain.user import UserDto
from src.config import settings
from src.exceptions import TokenExpiredException, InvalidTokenException


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

    @staticmethod
    async def decode_access_token(token: str) -> Dict[str, str]:
        try:
            payload = jwt.decode(token, settings.ACCESS_SECRET_KEY, algorithms=[settings.ALGORITHM])
            expire_time = datetime.fromtimestamp(payload["exp"]).replace(tzinfo=timezone.utc)
            if expire_time < datetime.now(timezone.utc):
                raise TokenExpiredException
            return payload
        except jwt.ExpiredSignatureError:
            raise TokenExpiredException
        except jwt.DecodeError:
            raise InvalidTokenException
