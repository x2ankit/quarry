from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, UserLogin
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user import User
from app.utils.security import hash_password, verify_password, create_access_token
from app.db.dependencies import get_db, get_current_user
router = APIRouter()


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    existing_user = db.execute(
        select(User).where(User.email == user.email)
    ).scalar_one_or_none()

    if existing_user:
        raise HTTPException(status_code=409, detail="Email already Registered")

    hashed_password = hash_password(user.password)
    new_user = User(email=user.email, hashed_password=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully"}


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    existing_user = db.execute(
        select(User).where(User.email == user.email)
    ).scalar_one_or_none()

    if not existing_user:
        raise HTTPException(status_code=400, detail="Invalid Email or Password")
    if not verify_password(user.password, existing_user.hashed_password):

        raise HTTPException(status_code=400, detail="Invalid Email or Password")

    access_token = create_access_token({"sub": str(existing_user.id)})

    return {
        "access_token" : access_token,
        "token_type" : "bearer"
    }


@router.get("/me")
def get_me(
    current_user: User = Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "email": current_user.email
    }

