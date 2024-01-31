from __future__ import annotations
from db.db import Base

from sqlalchemy import String, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy.sql import func

from sqlalchemy.dialects.postgresql import UUID


class Reservation(Base):
    __tablename__ = "reservations"

    reservation_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid()
    )

    user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False
    )
    room_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("rooms.room_id"), nullable=False
    )
    reservation_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    reservation_status: Mapped[str] = mapped_column(String(15), default="Active")
    reservation_price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    arrival_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    departure_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)

    adults: Mapped[int] = mapped_column(Numeric(5), nullable=False)
    children: Mapped[int] = mapped_column(Numeric(5), nullable=False)
