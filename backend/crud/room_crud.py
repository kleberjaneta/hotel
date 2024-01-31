from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.room_model import Room

from schemas.room_schema import RoomCreate, RoomSimple

from db.db import get_db

from uuid import UUID

from custom_logging import logger


def create_room(db: Session, room: RoomCreate) -> RoomSimple:
    try:
        new_room = Room(**room.dict())
        db.add(new_room)
        db.flush()
        db.commit()
        db.refresh(new_room)
        logger.info(f"Room {new_room.room_name} created")
        return new_room
    except Exception as e:
        db.rollback()
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


def get_all_rooms(db: Session) -> list[RoomSimple]:
    try:
        return db.query(Room).all()
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
