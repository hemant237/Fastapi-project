from fastapi import Depends , HTTPException ,status
from fastapi.security import HTTPBearer , HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User


import os


import jwt
from dotenv import load_dotenv
from pwdlib import PasswordHash
from datetime import datetime , timedelta , timezone


loaded = load_dotenv()

password_hash = PasswordHash.recommended()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = "HS256"
bearer_scheme=HTTPBearer()

def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    return password_hash.verify(
        plain_password,
        hashed_password
    )

def create_access_token(user_id : int) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    payload = {
        "sub": str(user_id),
        "type" : "access",
        "exp": expire
    }

    token = jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm = JWT_ALGORITHM
    )

    return token

def get_current_user(
        credentials : HTTPAuthorizationCredentials = Depends(bearer_scheme),
        db : Session =Depends(get_db)
):

    token = credentials.credentials
    try:
        payload = jwt.decode(
            token,
            JWT_SECRET_KEY,
            algorithms=[JWT_ALGORITHM]
        )

        user_id = payload.get("sub")
        token_type=payload.get("type")


        if user_id is None or token_type != "access":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail = "Invalid token"
            )

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )    

    user = db.get(User,int(user_id))

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not Found"
        )

    return user


def require_admin(
        current_user : User = Depends(get_current_user)
):
    if current_user.role != 'admin':
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Admin Access Required'
        )

    return current_user


def create_refresh_token (user_id : int) ->str:
    expire =datetime.now(timezone.utc) + timedelta(days=7)

    payload = {
        "sub" : str(user_id),
        "type" : "refresh",
        "exp" : expire
    }

    token=jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM
    )
    return token


