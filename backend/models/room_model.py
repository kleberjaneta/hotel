from __future__ import annotations
from db.db import Base

from sqlalchemy import String, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy.sql import func

from sqlalchemy.dialects.postgresql import UUID


class Room(Base):
    __tablename__ = "rooms"

    room_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid()
    )
    room_name: Mapped[str] = mapped_column(String(100), nullable=False)
    room_description: Mapped[str] = mapped_column(String(250), nullable=True)
    room_status: Mapped[str] = mapped_column(String(15), default="Available")
    room_capacity: Mapped[int] = mapped_column(Numeric(5), nullable=False)
    room_price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    room_type: Mapped[str] = mapped_column(String(50), nullable=False)

    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    # images: Mapped[List["Image"]] = relationship(back_populates="room")
