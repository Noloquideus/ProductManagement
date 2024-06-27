from typing import Literal
from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(find_dotenv(".env"))


class Settings(BaseSettings):
    MODE: Literal['DEV', 'TEST']

    TEST_DB_HOST: str
    TEST_DB_PORT: int
    TEST_DB_USER: str
    TEST_DB_PASS: str
    TEST_DB_NAME: str

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    REDIS_HOST: str
    REDIS_PORT: int

    ALGORITHM: str
    ACCESS_SECRET_KEY: str
    ACCESS_TTL_MINUTES: int

    SUPERADMIN_EMAIL: str
    SUPERADMIN_PHONE: str
    SUPERADMIN_FIRSTNAME: str
    SUPERADMIN_LASTNAME: str
    SUPERADMIN_PASSWORD: str
    SUPERADMIN_ACCESS_LEVEL: int

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def TEST_DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.TEST_DB_USER}:{self.TEST_DB_PASS}@{self.TEST_DB_HOST}:{self.TEST_DB_PORT}/{self.TEST_DB_NAME}"

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
