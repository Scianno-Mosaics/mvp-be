from fastapi import APIRouter
from mvp_be.models.message import Message
from mvp_be.services.jack_logic import handle_message

router = APIRouter()

@router.post("/echo")
async def jack(payload: Message):
    reply = await handle_message(payload.message)
    return {"Jack Said": reply}
