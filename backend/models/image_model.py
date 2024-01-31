from __future__ import annotations
from db.db import Base

from sqlalchemy import String, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy.sql import func

from sqlalchemy.dialects.postgresql import UUID


class Image(Base):
    __tablename__ = "images"

    image_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid()
    )
    image_url: Mapped[str] = mapped_column(String(250), nullable=False)
    # room_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), nullable=False)

    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    # room: Mapped["Room"] = relationship(back_populates="images")
