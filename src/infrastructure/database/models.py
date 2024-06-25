import uuid
from sqlalchemy import Column, UUID, String, DateTime, func
from sqlalchemy.dialects.postgresql import ARRAY, INTEGER
from src.infrastructure.database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    phone_number = Column(String, nullable=False, unique=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    access_level = Column(INTEGER, nullable=False, default=1)
    refresh_tokens = Column(ARRAY(String), nullable=True)
    date_created = Column(DateTime, nullable=False, default=func.now())
