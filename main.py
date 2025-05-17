from fastapi import FastAPI
from config import get_settings
from api.chat_routes import router as chat_router

settings = get_settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG,
)

app.include_router(chat_router, prefix="/api")
