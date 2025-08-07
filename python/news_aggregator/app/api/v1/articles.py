from fastapi import APIRouter

articles_router = APIRouter()

@articles_router.get("/")
def get_articles():
    return ["article1", "article2"]
