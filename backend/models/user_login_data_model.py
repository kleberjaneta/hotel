from __future__ import annotations
from db.db import Base

from typing import List

from sqlalchemy import String, ForeignKey, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy.sql import func

from db.db import Base

from sqlalchemy.dialects.postgresql import UUID


class UserLoginData(Base):
    __tablename__ = "user_login_data"
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    identification: Mapped[str] = mapped_column(String(50), nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(250), nullable=False)
    is_default_password: Mapped[int] = mapped_column(default=1)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())

    """ Relationships """
    # UserLoginData - User (one to One)
    user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.user_id"), primary_key=True
    )

    user: Mapped["User"] = relationship(back_populates="user_login_data")
