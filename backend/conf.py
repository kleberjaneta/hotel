from decouple import config
from pydantic import BaseSettings


class Settings(BaseSettings):
    ACCESS_TOKEN_DEFAULT_EXPIRE_MINUTES: int = config(
        "ACCESS_TOKEN_DEFAULT_EXPIRE_MINUTES"
    )
    GATEWAY_TIMEOUT: int = config("GATEWAY_TIMEOUT")
    DBMS: str = config("DBMS")
    DB_USER: str = config("DB_USER")
    DB_PASSWORD: str = config("DB_PASS")
    DB_HOST: str = config("DB_HOST")
    DB_PORT: str = config("DB_PORT")
    DB_NAME: str = config("DB_NAME")
    SECRET_KEY: str = config("SECRET_KEY")
    ALGORITHM: str = config("ALGORITHM")

    class Config:
        env_file = ".env"


settings = Settings()
