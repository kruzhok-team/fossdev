from fastapi import FastAPI
import threading
from app.router import router

from notifier import start_bot

# Start Telegram bot in a separate thread
threading.Thread(target=start_bot, daemon=True).start()

app = FastAPI()

app.include_router(router)