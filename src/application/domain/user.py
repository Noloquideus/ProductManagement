from typing import List
import phonenumbers
from pydantic import BaseModel, StrictStr, EmailStr, Field, field_validator
from src.exceptions import InvalidPhoneNumberException, InvalidPhoneNumberFormatException


class UserRegistration(BaseModel):
    phone_number: StrictStr = Field(
        title="Phone number",
        description="Phone number of the user",
        example="+79111111111")

    email: EmailStr = Field(
        title="Email",
        description="Email of the user",
        example="example@example.com")

    first_name: StrictStr = Field(
        title="First name",
        description="First name of the user",
        example="John")

    last_name: StrictStr = Field(
        title="Last name",
        description="Last name of the user",
        example="Doe")

    password: StrictStr = Field(
        title="Password",
        description="Password of the user",
        example="password",
        min_length=8,
        max_length=128)

    @field_validator('phone_number')
    def validate_phone_number(cls, phone_number):
        try:
            parsed_number = phonenumbers.parse(phone_number)
            if not phonenumbers.is_valid_number(parsed_number):
                raise InvalidPhoneNumberException
        except Exception as e:
            raise InvalidPhoneNumberFormatException from e
        return phone_number


class UserDto(BaseModel):
    id: str = None
    phone_number: str = None
    email: str = None
    first_name: str = None
    last_name: str = None
    password_hash: str = None
    access_level: int = None
    is_email_verified: bool = None
    refresh_tokens: List[str] = None
    date_created: str = None
