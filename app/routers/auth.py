from fastapi import APIRouter, Depends , status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.auth import RegisterRequest, UserResponse ,LoginRequest , RefreshTokenRequest

from app.models.user import User
from fastapi import HTTPException

from app.core.security import (verify_password , hash_password , create_access_token , get_current_user ,
                                require_admin , create_refresh_token, JWT_SECRET_KEY,JWT_ALGORITHM , hash_refresh_token,
                                verify_refresh_token , get_refresh_token_record)

from app.models.refresh_token import RefreshToken

from datetime import datetime , timedelta , timezone

import jwt


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
def register(
    user: RegisterRequest,
    db: Session = Depends(get_db)
):
    existing_user=db.query(User).filter(
        User.email==user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already Registered"
        )
    hashed_password=hash_password(user.password)

    db_user=User(
        email=user.email,
        password_hash=hashed_password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

@router.post("/login")
def login(
    user : LoginRequest,
    db : Session = Depends(get_db)
):
    existing_user=db.query(User).filter(
        User.email == user.email
    ).first()

    if not existing_user:
        raise HTTPException(
            status_code=401,
            detail= 'Invalid Email or Password'
        )

    password_correct = verify_password(
        user.password,existing_user.password_hash
    )

    if not password_correct:
        raise HTTPException(
            status_code=401,
            detail = "Invalid Email or Password"
        )

    access_token = create_access_token(existing_user.id)
    refresh_token = create_refresh_token(existing_user.id)

    refresh_token_record=RefreshToken(
        user_id=existing_user.id,
        token_hash=hash_refresh_token(refresh_token),
        expires_at=datetime.now(timezone.utc)+timedelta(days=7),
        revoked=False
    )

    db.add(refresh_token_record)
    db.commit()

    return {
        "access_token" : access_token,
        "refresh_token" : refresh_token,
        "token_type" : "bearer"
        }

@router.get("/me")
def get_me(
    current_user : User = Depends(get_current_user)
):
    return {
        "id" : current_user.id,
        "email": current_user.email
    }

@router.get("/admin_test")
def admin_test(
    current_user : User = Depends (require_admin)
):
    return {
        "meaasge": "Welcome Admin",
        "user" : current_user.email,
        "role" : current_user.role
    }


@router.post("/refresh")
def refresh_access_token(
    request : RefreshTokenRequest,
    db : Session = Depends(get_db)
):
    refresh_token_record=get_refresh_token_record(
        request.refresh_token,
        db
    )             

    new_access_token=create_access_token(refresh_token_record.user_id)

    return {
        "access_token":new_access_token,
        "token_type": "bearer"
    }


@router.post("/logout")
def logout(
    request : RefreshTokenRequest,
    db : Session = Depends(get_db)
):
   refresh_token_record=get_refresh_token_record(
       request.refresh_token,
       db 
   )

   refresh_token_record.revoked=True

   db.commit()

   return {
       "message" : "Logged out Successfully"
   }
    


        

