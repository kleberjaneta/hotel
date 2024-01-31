import jwt
from custom_logging import logger

from datetime import datetime, timedelta

from conf import settings


def generate_access_token(
    data: dict,
    expires_delta: timedelta = timedelta(
        minutes=settings.ACCESS_TOKEN_DEFAULT_EXPIRE_MINUTES
    ),
):
    expire = datetime.utcnow() + expires_delta
    token_data = {
        **data,
        "exp": expire,
    }

    encoded_jwt = jwt.encode(
        token_data, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )

    return encoded_jwt


def decode_access_token(authorization: str = None):
    try:
        return jwt.decode(
            authorization, settings.SECRET_KEY, algorithms=settings.ALGORITHM
        )
    except Exception as e:
        logger.error(e)
        return None
