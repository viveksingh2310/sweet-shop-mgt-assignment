from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    database_url: str

    JWT_SECRET: str = "super-secret-key"
    JWT_ALGORITHM: str = "HS256"

    model_config = ConfigDict(
        env_file=".env",
        extra="forbid", 
    )
settings = Settings()
