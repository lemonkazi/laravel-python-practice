from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.schemas.user import UserCreate, UserOut
from app.schemas.token import Token, TokenWithUser
from app.schemas.auth import LoginRequest
from app.services.auth_service import authenticate_user
from app.dao.user_dao import get_user_by_email, create_user

auth_router = APIRouter()

@auth_router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user)

@auth_router.post("/login", response_model=TokenWithUser)
def login(login_request: LoginRequest, db: Session = Depends(get_db)):
    access_token, refresh_token, user = authenticate_user(db, login_request.email, login_request.password)
    return TokenWithUser(
        access_token=access_token,
        refresh_token=refresh_token,
        user=UserOut(**user.__dict__)
    )

