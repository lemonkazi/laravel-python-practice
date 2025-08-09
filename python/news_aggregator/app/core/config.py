# app/core/config.py
# from pydantic import BaseSettings
from pydantic_settings import BaseSettings  # ✅ correct in Pydantic v2

from typing import List
from dotenv import load_dotenv
print("🔧 Loading environment variables...")
load_dotenv()
print("✅ .env loaded")

class Settings(BaseSettings):
    app_name: str = "News Aggregator API"
    app_version: str = "1.0.0"
    app_host: str = "0.0.0.0"
    app_port: int = 5001
    allowed_origins: List[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]
    PROJECT_NAME: str = "News Aggregator"
    MYSQL_USER: str = "user"
    MYSQL_PASSWORD: str = "secret"
    MYSQL_DB: str = "python_practice"
    MYSQL_HOST: str = "db"
    MYSQL_PORT: int = 3306
    jwt_secret_key: str  # ✅ Add this field

    class Config:
        env_file = ".env"
        extra = "ignore"  # ✅ Allow extra fields

print("📦 Instantiating settings...")
settings = Settings()
print("✅ Settings loaded")
