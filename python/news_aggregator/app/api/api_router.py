from fastapi import APIRouter
from .v1 import articles_router, auth_router

api_router = APIRouter()

api_router.include_router(articles_router, prefix="/articles", tags=["articles"])
api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
