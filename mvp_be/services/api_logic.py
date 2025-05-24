from fastapi import FastAPI, File, UploadFile
import os
import shutil
from datetime import datetime, UTC
import random
import httpx
import magic  # Ensure you have python-magic installed
from mvp_be.config import settings
import json


jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the web developer go broke? Because he used up all his cache.",
    "Why do programmers hate nature? It has too many bugs.",
]

async def handle_upload(file: UploadFile = File(...)):
    upload_dir = settings.UPLOAD_DIR if settings.UPLOAD_DIR is not None else "uploads"
    file_path = os.path.join(upload_dir, str(file.filename))

    # Save file to disk
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Get file metadata
    file_stat = os.stat(file_path)
    file_size = file_stat.st_size
    creation_time = datetime.fromtimestamp(file_stat.st_ctime).isoformat()

    # Detect file type
    mime = magic.Magic(mime=True)
    file_type = mime.from_file(file_path)

    result =  {
        "filename": file.filename,
        "size_bytes": file_size,
        "created_at": creation_time,
        "mime_type": file_type,
        "path": file_path,
    }
    return json.dumps(result)

async def handle_message(user_message: str) -> str:
    user_message = user_message.strip().lower()

    if "who is in space" in user_message:
        return await handle_space_query()

    elif "what time is it" in user_message:
        return handle_time_query()

    elif "tell me a joke" in user_message:
        return handle_joke_request()

    elif "help" in user_message or "what can i ask" in user_message:
        return handle_help_request()

    return handle_default_echo(user_message)


# === Handlers ===

async def handle_space_query() -> str:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(settings.ASTRONAUT_API_URL, timeout=settings.TIMEOUT_SECONDS)
            response.raise_for_status()
            data = response.json()
            people = data.get("people", [])
            count = data.get("number", 0)
            names = "\n".join([f"- {p['name']} ({p['craft']})" for p in people])
            return f"🧑‍🚀 There are {count} people in space:\n{names}"
    except Exception as e:
        return f"❌ Failed to fetch astronaut data: {str(e)}"


def handle_time_query() -> str:
    now = datetime.now(UTC).strftime("%H:%M UTC on %Y-%m-%d")
    return f"🕒 The current UTC time is {now}"


def handle_joke_request() -> str:
    return f"😂 {random.choice(jokes)}"


def handle_help_request() -> str:
    return (
        "🤖 You can ask me things like:\n"
        "- Who is in space\n"
        "- What time is it\n"
        "- Tell me a joke\n"
        "- (Or just say anything and I'll echo it!)"
    )


def handle_default_echo(message: str) -> str:
    return f"You said: '{message}'"
