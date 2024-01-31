from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class UserLoginData(BaseModel):
    username: str
    hashed_password: str
    is_default_password: int
    created_at: datetime
    user_id: UUID

    class Config:
        orm_mode = True


class UserLoginDataCredentials(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class ChangePassword(BaseModel):
    token: str
    password: str


class UserToken(BaseModel):
    user_id: str
    fullname: str
    username: str
    birthdate: datetime
    email: str
    phone: str
    user_role_id: str
    is_active: int
