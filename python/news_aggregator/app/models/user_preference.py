from sqlalchemy import Column, Integer, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.core.database import Base

class UserPreference(Base):
    __tablename__ = "user_preferences"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sources = Column(JSON, nullable=True)      # Example: ["BBC", "CNN"]
    categories = Column(JSON, nullable=True)   # Example: ["Politics", "Sports"]
    authors = Column(JSON, nullable=True)      # Example: ["John Doe"]

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relationship
    user = relationship("User", back_populates="preference")
