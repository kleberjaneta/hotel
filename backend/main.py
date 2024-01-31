from fastapi import FastAPI, Request, Depends
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import request_validation_exception_handler
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from db.db import engine, get_db, Base

from custom_logging import logger

import pandas as pd
from os import path

from routes import rooms, users

pathname = path.dirname(__file__)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Hotel Management API",
    description="API for a hotel management system",
    version="0.1.0",
)


app.include_router(
    rooms.router,
    prefix="/api",
    tags=["rooms"],
)

app.include_router(
    users.router,
    prefix="/api",
    tags=["users"],
)
