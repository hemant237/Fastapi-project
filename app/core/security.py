from fastapi import Depends , HTTPException ,status
from fastapi.security import HTTPBearer , HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.models.refresh_token import RefreshToken
from app.models.password_reset_token import PasswordResetToken


import os
import secrets


import jwt
from dotenv import load_dotenv
from pwdlib import PasswordHash
from datetime import datetime , timedelta , timezone

load_dotenv()

password_hash = PasswordHash.recommended()
def hash_refresh_token(token:str) ->str:
    return password_hash.hash(token)


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


def verify_refresh_token(
    plain_token: str,
    hashed_token: str
) -> bool:
    return password_hash.verify(
        plain_token,
        hashed_token
    )

def get_refresh_token_record(
        token : str,
        db : Session
) ->RefreshToken:

    try:
        payload = jwt.decode(
            token,
            JWT_SECRET_KEY,
            algorithms=[JWT_ALGORITHM]
        )

        user_id=payload.get("sub")
        token_type=payload.get("type")

        if user_id is None or token_type != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                status="Invalid refresh token"
            )    

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid refresh token'
        )    

    refresh_tokens=db.query(RefreshToken).filter(RefreshToken.user_id==int(user_id)).all()

    for stored_token in refresh_tokens:
        if verify_refresh_token(
            token,
            stored_token.token_hash
        ):
            if stored_token.revoked:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Refresh token has been revoked"
                )

            if stored_token.expires_at<=datetime.now(timezone.utc):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Refresh Token has Expired"
                )

            return stored_token

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHOROZED,
        detail="Refresh session not found"
    )    


def create_password_reset_token() ->str:
    return secrets.token_urlsafe(32)


def get_password_reset_token_record(
        plain_token : str,
        db :Session
):
    reset_tokens=db.query(PasswordResetToken).all()

    for stored_tokens in reset_tokens:
        if verify_refresh_token(plain_token,stored_tokens.token_hash):
            return stored_tokens


    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid password reset token"
    )    


