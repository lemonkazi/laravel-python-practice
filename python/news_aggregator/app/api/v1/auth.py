from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.schemas.user import UserCreate, UserOut
from app.schemas.token import Token, TokenWithUser, TokenRefreshResponse
from app.schemas.auth import LoginRequest, RefreshRequest
from app.services.auth_service import authenticate_user, refresh_token, revoke_token
from app.dao.user_dao import UserDAO

auth_router = APIRouter()

@auth_router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = UserDAO(db).get_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return UserDAO(db).create(user)

@auth_router.post("/login", response_model=TokenWithUser)
def login(login_request: LoginRequest, db: Session = Depends(get_db)):
    access_token, refresh_token, user = authenticate_user(db, login_request.email, login_request.password)
    return TokenWithUser(
        access_token=access_token,
        refresh_token=refresh_token,
        user=UserOut(
            id=user.id,
            name=user.name,
            email=user.email
        )
    )

@auth_router.post("/refresh", response_model=TokenRefreshResponse)
def refresh(refresh_request: RefreshRequest, db: Session = Depends(get_db)):
    access_token = refresh_token(db, refresh_request.refresh_token)
    return {"access_token": access_token}

@auth_router.post("/logout")
def logout(refresh_request: RefreshRequest, db: Session = Depends(get_db)):
    revoke_token(db, refresh_request.refresh_token)
    return {"message": "Successfully logged out"}

