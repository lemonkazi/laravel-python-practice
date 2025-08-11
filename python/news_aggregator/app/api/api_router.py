from fastapi import APIRouter
from app.api.v1 import health, articles, auth
from app.api import test_db
from app.api.middlewares.auth import get_current_user

api_router = APIRouter(prefix="/v1")

api_router.include_router(health.router, tags=["Health"])
api_router.include_router(auth.auth_router, prefix="/auth", tags=["Auth"])
api_router.include_router(articles.articles_router, prefix="/articles")
api_router.include_router(test_db.router, tags=["db-test"])
