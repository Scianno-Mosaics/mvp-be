from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import field_validator
from typing import List
import os



class Settings(BaseSettings):
    model_config = SettingsConfigDict(
    env_file=".env",
    extra="ignore"
    )

    PROJECT_NAME: str = "SciAnno API mvp"
    VERSION: str = "0.1.0"
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    ASTRONAUT_API_URL: str = "http://api.open-notify.org/astros.json"
    TIMEOUT_SECONDS: int = int(os.getenv("TIMEOUT_SECONDS", "5"))
    UPLOAD_DIR: str = os.getenv("UPLOAD_DIR", "uploads")
    CORS_ORIGINS: list[str] = ["https://talk.dilly.cloud", "http://localhost:3000"]  # Add this line

    @field_validator("CORS_ORIGINS", mode="before")
    
    @classmethod
    def split_cors_origins(cls, value):
        if isinstance(value, str):
            return [origin.strip() for origin in value.split(",")]
        return value

settings = Settings()
