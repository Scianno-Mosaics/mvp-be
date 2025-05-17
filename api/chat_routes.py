from fastapi import APIRouter
from models.message import Message
from services.chat_logic import handle_message

router = APIRouter()

@router.post("/echo")
async def echo(payload: Message):
    reply = await handle_message(payload.message)
    return {"reply": reply}
