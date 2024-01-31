from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class RoomBase(BaseModel):
    room_name: str
    room_description: str
    room_status: str
    room_capacity: int
    room_price: float
    room_type: str


class RoomCreate(RoomBase):
    pass


class RoomSimple(RoomBase):
    room_id: UUID

    class Config:
        orm_mode = True


class Room(RoomSimple):
    created_at: datetime

    class Config:
        orm_mode = True
