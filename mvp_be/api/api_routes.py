from fastapi import APIRouter, UploadFile, File
from mvp_be.models.message import Message
from mvp_be.services.api_logic import handle_message
from mvp_be.services.api_logic import handle_upload


router = APIRouter()

@router.post("/echo")
async def echo(payload: Message):
    reply = await handle_message(payload.message)
    return {"reply": reply}

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    reply = await handle_upload(file)
    return {"reply": reply}


