from sqlalchemy import Column, Integer, ForeignKey, JSON, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base
from sqlalchemy.sql import func


class UserPreference(Base):
    __tablename__ = "user_preferences"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sources = Column(JSON, nullable=True)      # Example: ["BBC", "CNN"]
    categories = Column(JSON, nullable=True)   # Example: ["Politics", "Sports"]
    authors = Column(JSON, nullable=True)      # Example: ["John Doe"]
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relationship
    user = relationship("User", back_populates="preference")
