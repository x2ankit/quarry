from app.db.database import SessionLocal
from fastapi import Depends
from app.utils.security import oauth2_scheme, verify_access_token
from sqlalchemy import select
from app.models.user import User
from sqlalchemy.orm import Session
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def get_current_user_id(token: str = Depends(oauth2_scheme)):
    return verify_access_token(token)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    user_id = verify_access_token(token)

    current_user = db.execute(
        select(User).where(
            User.id == user_id
        )
    ).scalar_one_or_none()

    return current_user