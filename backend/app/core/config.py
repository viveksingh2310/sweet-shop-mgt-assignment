from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from typing import Set
class Settings(BaseSettings):
    database_url: str

    JWT_SECRET: str = "super-secret-key"
    JWT_ALGORITHM: str = "HS256"
   # 👇 admin users defined here
    ADMIN_EMAILS: Set[str] = {
        "admin@example.com",
        "viveksingh@example.com"
    }
    model_config = ConfigDict(
        env_file=".env",
        extra="forbid", 
    )
settings = Settings()
