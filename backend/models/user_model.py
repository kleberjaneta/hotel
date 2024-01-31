from __future__ import annotations
from db.db import Base

from typing import List

from sqlalchemy import String, ForeignKey, Integer, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy.sql import func

from db.db import Base

from sqlalchemy.dialects.postgresql import UUID


class User(Base):
    __tablename__ = "users"
    user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid()
    )
    fullname: Mapped[str] = mapped_column(String(250), nullable=False)
    birthday: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    email: Mapped[str] = mapped_column(String(250), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(50), nullable=False)
    cellphone_number: Mapped[str] = mapped_column(String(50), nullable=False)
    is_active: Mapped[int] = mapped_column(default=1)
    status: Mapped[str] = mapped_column(String(50), default="Active")

    # Foreign Keys
    user_role_id = mapped_column(String(50), nullable=False)

    genre_code = mapped_column(String(1), nullable=False)

    # Relationships

    # User - UserLoginData (one to One)
    user_login_data: Mapped["UserLoginData"] = relationship(back_populates="user")
