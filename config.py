import os
from functools import lru_cache

class Settings:
    PROJECT_NAME: str = "Chat Echo API mvp"
    VERSION: str = "0.1.0"
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    ASTRONAUT_API_URL: str = "http://api.open-notify.org/astros.json"
    TIMEOUT_SECONDS: int = int(os.getenv("TIMEOUT_SECONDS", "5"))

@lru_cache()
def get_settings() -> Settings:
    return Settings()
