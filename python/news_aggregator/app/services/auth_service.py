from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.dao.user_dao import UserDAO
from app.utils.security import verify_password
from app.utils.jwt import create_access_token, create_refresh_token
from app.schemas.token import Token
from app.models.refresh_token import RefreshToken
from jose import JWTError, jwt
from app.core.config import settings

def authenticate_user(db: Session, email: str, password: str) -> tuple:
    user = UserDAO(db).get_by_email(email)
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")

    access_token = create_access_token(data={"sub": user.email})
    refresh_token, expires_at = create_refresh_token(data={"sub": user.email})

    # Store refresh token in database
    db_refresh_token = RefreshToken(
        user_id=user.id,
        token=refresh_token,
        expires_at=expires_at,
        revoked=False
    )
    db.add(db_refresh_token)
    db.commit()

    return access_token, refresh_token, user

def refresh_token(db: Session, token: str) -> str:
    stored_token = db.query(RefreshToken).filter(RefreshToken.token == token).first()
    if not stored_token or stored_token.revoked:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    try:
        payload = jwt.decode(
            token,
            settings.jwt_refresh_secret_key,
            algorithms=[settings.jwt_algorithm]
        )
        email = payload.get("sub")
        if not email:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = UserDAO(db).get_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return create_access_token(data={"sub": user.email})

def revoke_token(db: Session, token: str) -> None:
    stored_token = db.query(RefreshToken).filter(RefreshToken.token == token).first()
    if stored_token:
        stored_token.revoked = True
        db.commit()
        db.refresh(stored_token)
