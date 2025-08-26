# app/main.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from .api import api_router
from app.api.api_router import api_router
from .core.config import settings
from .core import logging_config  # <-- triggers logger setup
import logging
from fastapi.exceptions import RequestValidationError
from .utils.exception_handlers import validation_exception_handler
from app.api import test_db


# app = FastAPI(
#     title="News Aggregator API",
#     version="1.0.0"
# )
from fastapi.openapi.models import APIKey
from fastapi.openapi.utils import get_openapi

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

# Add security scheme for Swagger
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
        
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        routes=app.routes,
    )
    
    # Merge existing components with our security scheme
    components = openapi_schema.setdefault("components", {})
    components.setdefault("securitySchemes", {}).update({
        "bearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    })
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

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
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the News Aggregator API - Reloaded"}

@app.get("/health-check")
def health_check():
    return {"status": "ok"}
