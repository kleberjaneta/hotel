from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from db.db import get_db

# Position
from schemas.room_schema import RoomCreate, RoomSimple
from crud.room_crud import create_room, get_all_rooms

router = APIRouter(
    prefix="/rooms",
    tags=["rooms"],
    responses={404: {"description": "Not found"}},
)


@router.post("", response_model=RoomSimple)
async def create_position_endpoint(room: RoomCreate, db: Session = Depends(get_db)):
    return create_room(db, room)


@router.get("", response_model=list[RoomSimple])
async def get_positions_endpoint(db: Session = Depends(get_db)):
    return get_all_rooms(db)
