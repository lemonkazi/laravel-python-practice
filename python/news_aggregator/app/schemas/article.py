from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class PaginationQuery(BaseModel):
    page: int = Field(1, ge=1)
    limit: int = Field(10, ge=1, le=100)
    search: Optional[str] = None
    category: Optional[str] = None
    source: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

class ArticleBase(BaseModel):
    title: str
    content: str
    category: str
    source: str
    author: str | None = None
    published_at: datetime | None = None

class ArticleCreate(ArticleBase):
    pass

class ArticleOut(ArticleBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class ArticlePagination(BaseModel):
    data: list[ArticleOut]
    pagination: dict
