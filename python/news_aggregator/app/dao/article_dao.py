from sqlalchemy.orm import Session
from app.models.article import Article
from sqlalchemy import or_
from app.dao.base_dao import BaseDAO

class ArticleDAO(BaseDAO[Article]):
    def __init__(self, db: Session):
        super().__init__(Article, db)

    def find_all(self, page: int = 1, limit: int = 10, filters: dict = None):
        query = self.db.query(self.model)
        
        if filters:
            if 'search' in filters:
                search = f"%{filters['search']}%"
                query = query.filter(
                    or_(
                        self.model.title.ilike(search),
                        self.model.content.ilike(search)
                    )
                )
            if 'category' in filters:
                query = query.filter(self.model.category == filters['category'])
            if 'source' in filters:
                query = query.filter(self.model.source == filters['source'])
            if 'date_range' in filters:
                start, end = filters['date_range']
                if start:
                    query = query.filter(self.model.published_at >= start)
                if end:
                    query = query.filter(self.model.published_at <= end)

        total = query.count()
        articles = query.order_by(self.model.published_at.desc())\
                      .offset((page - 1) * limit)\
                      .limit(limit)\
                      .all()

        return {
            "data": articles,
            "total": total,
            "page": page,
            "limit": limit,
            "total_pages": (total + limit - 1) // limit
        }
