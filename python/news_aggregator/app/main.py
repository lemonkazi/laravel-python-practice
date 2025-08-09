# app/main.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import api_router
from .core.config import settings
from .core import logging_config  # <-- triggers logger setup
import logging
from fastapi.exceptions import RequestValidationError
from .utils.exception_handlers import validation_exception_handler
from app.api import test_db


app = FastAPI(
    title="News Aggregator API",
    version="1.0.0"
)
# app = FastAPI(
#     title=settings.app_name,
#     version=settings.app_version,
# )

app.add_exception_handler(RequestValidationError, validation_exception_handler)

# Logging config
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)
logger.info("Starting the app...")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    # allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router)
app.include_router(test_db.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the News Aggregator API - Reloaded"}

@app.get("/health-check")
def health_check():
    return {"status": "ok"}
