from sqlalchemy import Column, Integer, String, Text, DateTime
from app.core.database import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    summary = Column(Text, nullable=True)
    content = Column(Text, nullable=True)
    source = Column(String, nullable=True)
    author = Column(String, nullable=True)
    published_at = Column(DateTime, nullable=True)
    category = Column(String, nullable=True)
