from datetime import datetime, UTC
import random
import httpx
from mvp_be.config import settings


async def handle_message(user_message: str) -> str:
    user_message = user_message.strip().lower()

    return handle_default_echo(user_message)


def handle_default_echo(message: str) -> str:
    return f"You said: '{message}'"
