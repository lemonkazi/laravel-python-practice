from sqlalchemy.orm import Session
from app.models.article import Article
from sqlalchemy import and_, or_, func

class ArticleDAO:
    def __init__(self, db: Session):
        self.db = db

    def find_all(self, page: int = 1, limit: int = 10, filters: dict = None):
        query = self.db.query(Article)
        
        if filters:
            if 'search' in filters:
                search = f"%{filters['search']}%"
                query = query.filter(
                    or_(
                        Article.title.ilike(search),
                        Article.content.ilike(search)
                    )
                )
            if 'category' in filters:
                query = query.filter(Article.category == filters['category'])
            if 'source' in filters:
                query = query.filter(Article.source == filters['source'])
            if 'date_range' in filters:
                start, end = filters['date_range']
                if start:
                    query = query.filter(Article.published_at >= start)
                if end:
                    query = query.filter(Article.published_at <= end)

        total = query.count()
        articles = query.order_by(Article.published_at.desc())\
                      .offset((page - 1) * limit)\
                      .limit(limit)\
                      .all()

        return {
            "data": articles,
            "total": total
        }
