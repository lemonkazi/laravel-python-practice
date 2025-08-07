from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "News Aggregator"
    MYSQL_USER: str = "user"
    MYSQL_PASSWORD: str = "secret"
    MYSQL_DB: str = "laravel_test"
    MYSQL_HOST: str = "db"
    MYSQL_PORT: int = 3306

    class Config:
        env_file = ".env"

settings = Settings()
