from fastapi import APIRouter
from mvp_be.models.message import Message
from mvp_be.services.chat_logic import handle_message

router = APIRouter()

@router.post("/echo")
async def echo(payload: Message):
    reply = await handle_message(payload.message)
    return {"reply": reply}
