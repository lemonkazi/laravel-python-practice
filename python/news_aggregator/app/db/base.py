from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from app.models.article import Article
from app.models.user import User
from app.models.user_preference import UserPreference
from app.models.refresh_token import RefreshToken