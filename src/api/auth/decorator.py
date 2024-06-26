from functools import wraps
from typing import Callable
from src.exceptions import InvalidTokenException, TokenExpiredException
from src.infrastructure.utils.token_service import TokenService


def require_min_access_level(min_access_level: int):
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            request = args[0]
            access_token = request.cookies.get("access_token")
            if not access_token:
                raise InvalidTokenException
            try:
                payload = await TokenService.decode_access_token(access_token)
                user_access_level = payload.get("access_level")
                if int(user_access_level) < min_access_level:
                    raise InvalidTokenException
            except (InvalidTokenException, TokenExpiredException) as e:
                raise e
            return await func(*args, **kwargs)

        return wrapper

    return decorator
