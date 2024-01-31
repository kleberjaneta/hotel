from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from db.db import get_db

# Role
from schemas.user import UserCreate, UserSimple
from crud.user_crud import create_user, get_all_users

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.post("", response_model=UserSimple)
async def create_users_endpoint(user_role: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user_role)


@router.get("", response_model=list[UserSimple])
async def get_users_endpoint(
    db: Session = Depends(get_db), page: int = 0, search: str = None
):
    return get_all_users(db, page, search)
