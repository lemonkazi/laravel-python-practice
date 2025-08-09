from fastapi import APIRouter
from app.api.v1 import health, articles, auth
from app.api import test_db

api_router = APIRouter()

api_router.include_router(health.router, prefix="/v1")
api_router.include_router(auth.router, prefix="/v1/auth", tags=["Auth"])
api_router.include_router(articles.router, prefix="/v1/articles", tags=["Articles"])
api_router.include_router(test_db.router, tags=["db-test"])
