from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.middlewares.auth import get_current_user
from app.models.user import User
from app.db.deps import get_db

articles_router = APIRouter()

from app.schemas.article import ArticlePagination, PaginationQuery
from app.dao.article_dao import ArticleDAO
from sqlalchemy import or_

@articles_router.get("/", tags=["Articles"], response_model=ArticlePagination)
def get_articles(query: PaginationQuery = Depends(), db: Session = Depends(get_db)):
    """Get paginated articles with filters"""
    dao = ArticleDAO(db)
    
    # Build filters
    filters = {}
    if query.search:
        filters['search'] = query.search
    if query.category:
        filters['category'] = query.category
    if query.source:
        filters['source'] = query.source
    if query.start_date or query.end_date:
        filters['date_range'] = (query.start_date, query.end_date)

    result = dao.find_all(
        page=query.page,
        limit=query.limit,
        filters=filters
    )
    
    return {
        "data": result["data"],
        "pagination": {
            "total": result["total"],
            "page": query.page,
            "limit": query.limit,
            "total_pages": (result["total"] + query.limit - 1) // query.limit
        }
    }

@articles_router.get("/{id}", tags=["Articles"])
def get_by_id(id: int):
    """Get article by ID (public)"""
    return {"id": id, "title": "Sample Article"}

from app.schemas.article import ArticleCreate, ArticleOut
from app.models.article import Article
from app.db.deps import get_db
from sqlalchemy.orm import Session

@articles_router.post("/", tags=["Articles"], response_model=ArticleOut, dependencies=[Depends(get_current_user)])
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    """Create new article (authenticated)"""
    db_article = Article(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

@articles_router.put("/{id}", tags=["Articles"], dependencies=[Depends(get_current_user)])
def update_article(id: int):
    """Update article (authenticated)"""
    return {"message": f"Article {id} updated"}

@articles_router.delete("/{id}", tags=["Articles"], dependencies=[Depends(get_current_user)])
def delete_article(id: int):
    """Delete article (authenticated)"""
    return {"message": f"Article {id} deleted"}

@articles_router.get("/feed/personalized", tags=["Articles"], dependencies=[Depends(get_current_user)])
def personalized_feed():
    """Get personalized feed (authenticated)"""
    return ["personalized_article1", "personalized_article2"]
