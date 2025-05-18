from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Add this import
from mvp_be.api.chat_routes import router as chat_router
from mvp_be.api.jack_routes import router as jack_router
from mvp_be.config import settings


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG,
)

# Add CORS middleware using origins from config
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/api")
app.include_router(jack_router, prefix="/jack")
