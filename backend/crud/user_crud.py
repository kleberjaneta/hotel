from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.user_model import User as UserModel
from models.user_login_data_model import UserLoginData as UserLoginDataModel

from schemas.user import UserCreate, UserSimple

from auth import password, token

from uuid import UUID


def create_user(db: Session, user: UserCreate):
    try:
        login_data_in_db = (
            db.query(UserLoginDataModel)
            .filter(UserLoginDataModel.username == user.username)
            .first()
        )

        if login_data_in_db:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Username already exists"
            )

        db_user = UserModel(
            fullname=user.fullname,
            birthday=user.birthday,
            email=user.email,
            phone_number=user.phone_number,
            cellphone_number=user.cellphone_number,
            user_role=user.user_role,
            genre_code=user.genre_code,
        )

        db.add(db_user)
        db.flush()

        hash_password = password.get_password_hash("P@ssw0rd")

        db_user_login_data = UserLoginDataModel(
            username=user.username,
            identification=user.identification,
            hashed_password=hash_password,
            user_id=db_user.user_id,
        )

        db.add(db_user_login_data)
        db.flush()

        db.commit()
        db.refresh(db_user)
        user = UserSimple.from_orm(db_user)
        user.username = db_user_login_data.username
        user.identification = db_user_login_data.identification
        return user
    except HTTPException as e:
        db.rollback()
        raise e
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


def get_all_users(db: Session, page: int, search: str):
    try:
        skip = page * 10
        limit = 10
        users = db.query(UserModel).offset(skip).limit(limit).all()
        # print(users[0].__dict__)
        for user in users:
            user.username = user.user_login_data.username
            user.identification = user.user_login_data.identification
            # print(user.genre)
        # print(type(users[0]))
        # print(users[0].__dict__)

        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def login_user(db: Session, username: str, password: str):
    try:
        user_login_data = (
            db.query(UserLoginDataModel)
            .filter(UserLoginDataModel.username == username)
            .first()
        )

        if not user_login_data and not password.verify_password(
            password, user_login_data.hashed_password
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found"
            )

        user = (
            db.query(UserModel)
            .filter(UserModel.user_id == user_login_data.user_id)
            .first()
        )

        user_token = token.generate_access_token(
            data={
                "user_id": str(user.user_id),
                "fullname": user.fullname,
                "username": user_login_data.username,
                "birthdate": user.birthday.strftime("%Y-%m-%d"),
                "email": user.email,
                "phone": user.phone_number,
                "user_role_id": str(user.user_role_id),
                "is_active": user.is_active,
                "status": user.status,
            }
        )

        return {
            "msg": "Login successful",
            "token": user_token,
            "is_default": user_login_data.is_default_password,
            "is_active": user.is_active,
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
