from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class UserBase(BaseModel):
    fullname: str
    birthday: datetime
    email: str
    phone_number: str
    cellphone_number: str
    genre_code: str


class UserCreate(UserBase):
    user_role: str
    identification: str

    username: str
    password: str


class UserSimple(UserBase):
    user_id: UUID
    role: str
    is_active: int
    username: str
    identification: str

    class Config:
        orm_mode = True


class UserUpdate(UserCreate):
    user_id: str


class UserDelete(BaseModel):
    user_id: str
