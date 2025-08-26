from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.schemas.user import UserCreate, UserOut
from app.dao.user_dao import UserDAO
from app.api.base_handler import BaseHandler
from app.models.user import User
from app.api.middlewares.auth import get_current_user

class UserHandler(BaseHandler[User, UserCreate, UserCreate]):
    def __init__(self):
        super().__init__(UserDAO)
        self.router = APIRouter()
        self.router.add_api_route(
            "/users", self.get_all, methods=["GET"], response_model=list[UserOut],
            dependencies=[Depends(get_current_user)], tags=["Users"]
        )
        self.router.add_api_route(
            "/users/{id}", self.get, methods=["GET"], response_model=UserOut,
            dependencies=[Depends(get_current_user)], tags=["Users"]
        )
        self.router.add_api_route(
            "/users", self.create, methods=["POST"], response_model=UserOut,
            dependencies=[Depends(get_current_user)], tags=["Users"]
        )
        self.router.add_api_route(
            "/users/{id}", self.update, methods=["PUT"], response_model=UserOut,
            dependencies=[Depends(get_current_user)], tags=["Users"]
        )
        self.router.add_api_route(
            "/users/{id}", self.delete, methods=["DELETE"],
            dependencies=[Depends(get_current_user)], tags=["Users"]
        )
        self.router.add_api_route(
            "/users/me", self.get_me, methods=["GET"], response_model=UserOut,
            dependencies=[Depends(get_current_user)], tags=["Users"]
        )

    def get_me(self, user: User = Depends(get_current_user)):
        """Get current user details"""
        return user

user_handler = UserHandler()
user_router = user_handler.router
