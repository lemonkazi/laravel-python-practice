from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.middlewares.auth import get_current_user
from app.models.user import User
from app.db.deps import get_db
from app.schemas.article import ArticlePagination, PaginationQuery
from app.dao.article_dao import ArticleDAO
from sqlalchemy import or_
from app.schemas.article import ArticleCreate, ArticleOut
from app.models.article import Article
from app.api.base_handler import BaseHandler


class ArticleHandler(BaseHandler[Article, ArticleCreate, ArticleCreate]):
    def __init__(self):
        super().__init__(ArticleDAO)
        self.router = APIRouter()
        self.router.add_api_route(
            "/", self.get_articles, methods=["GET"], tags=["Articles"], response_model=ArticlePagination
        )
        self.router.add_api_route(
            "/{id}", self.get_by_id, methods=["GET"], tags=["Articles"]
        )
        self.router.add_api_route(
            "/", self.create_article, methods=["POST"], tags=["Articles"], response_model=ArticleOut, dependencies=[Depends(get_current_user)]
        )
        self.router.add_api_route(
            "/{id}", self.update_article, methods=["PUT"], tags=["Articles"], dependencies=[Depends(get_current_user)]
        )
        self.router.add_api_route(
            "/{id}", self.delete_article, methods=["DELETE"], tags=["Articles"], dependencies=[Depends(get_current_user)]
        )
        self.router.add_api_route(
            "/feed/personalized", self.personalized_feed, methods=["GET"], tags=["Articles"], dependencies=[Depends(get_current_user)]
        )

    def get_articles(self, query: PaginationQuery = Depends(), db: Session = Depends(get_db)):
        """Get paginated articles with filters"""
        dao = self.dao(db)

        # Build filters
        filters = {}
        if query.search:
            filters["search"] = query.search
        if query.category:
            filters["category"] = query.category
        if query.source:
            filters["source"] = query.source
        if query.start_date or query.end_date:
            filters["date_range"] = (query.start_date, query.end_date)

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

    def get_by_id(self, id: int, db: Session = Depends(get_db)):
        """Get article by ID (public)"""
        dao = self.dao(db)
        article = dao.get(id)
        if not article:
            raise HTTPException(status_code=404, detail="Article not found")
        return article

    def create_article(self, article: ArticleCreate, db: Session = Depends(get_db)):
        """Create new article (authenticated)"""
        dao = self.dao(db)
        return dao.create(article)

    def update_article(self, id: int, article: ArticleCreate, db: Session = Depends(get_db)):
        """Update article (authenticated)"""
        dao = self.dao(db)
        return dao.update(id, article)

    def delete_article(self, id: int, db: Session = Depends(get_db)):
        """Delete article (authenticated)"""
        dao = self.dao(db)
        return dao.delete(id)

    def personalized_feed(self):
        """Get personalized feed (authenticated)"""
        return ["personalized_article1", "personalized_article2"]

article_handler = ArticleHandler()
articles_router = article_handler.router
