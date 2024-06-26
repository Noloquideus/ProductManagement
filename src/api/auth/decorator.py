from typing import Callable
from functools import wraps
from src.exceptions import InvalidTokenException, InsufficientAccessLevelException
from src.infrastructure.utils.token_service import TokenService


def require_min_access_level(min_access_level: int):
    """
       Minimal level decorator providing access for routes and token validation

       Args:
           min_access_level (int): The minimum access level required to access the route.

       Returns:
           Callable: The decorated function with access level enforcement.

       Example:
           @app.get("/ping")
            @require_min_access_level(min_access_level=1)
            async def ping(access_token: str = Cookie('access_token')):
                return {"message": "pong"}
       """
    def decorator(func: Callable):
        @wraps(func)
        async def decorated(*args, access_token, **kwargs):
            try:
                payload = await TokenService.decode_access_token(access_token)
            except Exception as e:
                raise InvalidTokenException

            access_level = payload.get("access_level", 0)
            print(access_level)

            if access_level < min_access_level:
                raise InsufficientAccessLevelException

            return await func(*args, **kwargs)
        return decorated
    return decorator
