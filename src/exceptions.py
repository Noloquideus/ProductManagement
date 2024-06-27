from fastapi import HTTPException, status


class DefaultException(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)

    def __str__(self):
        return f'{self.status_code}: {self.detail}'


class InvalidPhoneNumberException(DefaultException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid phone number')


class InvalidPhoneNumberFormatException(DefaultException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid phone number format')


class InvalidCredentialsException(DefaultException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials')


class UserAlreadyExistsException(DefaultException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail='User already exists')


class InvalidPasswordException(DefaultException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid password')


class TokenExpiredException(DefaultException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token expired')


class InvalidTokenException(DefaultException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')


class InsufficientAccessLevelException(DefaultException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient access level")


class CategoryAlreadyExistsException(DefaultException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail='Category already exists')


class CategoryNotFoundException(DefaultException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail='Category not found')
