from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

import os

DATABASE_URL = (
    f"mysql+pymysql://{settings.MYSQL_USER}:{settings.MYSQL_PASSWORD}"
    f"@{settings.MYSQL_HOST}:{settings.MYSQL_PORT}/{settings.MYSQL_DB}"
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

import logging

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        logging.info("Database session created")
        yield db
    except Exception as e:
        logging.error(f"Database session error: {e}")
        raise
    finally:
        logging.info("Database session closed")
        db.close()
