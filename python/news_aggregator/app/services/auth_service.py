from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.dao.user_dao import get_user_by_email
from app.utils.security import verify_password
from app.utils.jwt import create_access_token, create_refresh_token
from app.schemas.token import Token

def authenticate_user(db: Session, email: str, password: str) -> tuple:
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")

    access_token = create_access_token(data={"sub": user.email})
    refresh_token = create_refresh_token(data={"sub": user.email})

    return access_token, refresh_token, user
