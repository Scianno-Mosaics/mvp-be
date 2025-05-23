from fastapi import FastAPI, File, UploadFile
import os
import shutil
from datetime import datetime

from fastapi.middleware.cors import CORSMiddleware  # Add this import
from mvp_be.api.api_routes import router as api_router
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


os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

app.include_router(api_router, prefix="/api")
app.include_router(jack_router, prefix="/jack")
