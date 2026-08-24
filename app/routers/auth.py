from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.auth import RegisterRequest, UserResponse ,LoginRequest

from app.models.user import User
from fastapi import HTTPException

from app.core.security import (verify_password , hash_password , create_access_token , get_current_user ,
                                require_admin , create_refresh_token)


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
            status_code=404,
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
        "id :" : current_user.id,
        "email :": current_user.email
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
    