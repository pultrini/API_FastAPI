from datetime import datetime, timedelta
from http import HTTPStatus
from zoneinfo import ZoneInfo

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import DecodeError, decode, encode
from pwdlib import PasswordHash
from sqlalchemy import select
from sqlalchemy.orm import Session

from semana_da_fisica.database import get_session
from semana_da_fisica.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

SECRET_KEY = 'SenhaSecreta'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = PasswordHash.recommended()


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(tz=ZoneInfo('UTC')) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({'exp': expire})

    encode_jwp = encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encode_jwp


def get_current_user(
    session: Session = Depends(get_session),
    token: str = Depends(oauth2_scheme),
):
    credential_exceptions = HTTPException(
        status_code=HTTPStatus.UNAUTHORIZED,
        headers={'WWW-Authenticate': 'Bearer'},
        detail='Could not validate credentials',
    )

    try:
        payload = decode(token, SECRET_KEY, algorithms=ALGORITHM)
        subject_email = payload.get('sub')
        if not subject_email:
            raise credential_exceptions
    except DecodeError:
        raise credential_exceptions

    user = session.scalar(select(User).where(User.email == subject_email))
    if not user:
        raise credential_exceptions
    return user
