from dotenv import load_dotenv

load_dotenv("/home/carlos-rian/Documentos/project/telegram-bot-async/.env")

from fastapi import FastAPI, Depends
from app.database import instance
from app.database import connect
from app.database import model
from app.schema import RequestTelegramWebhook, ResponseTelegramWebhook
from app.controller import new_message

app = FastAPI(title="Telegram Async - Fast Api")

model.init_app()
db = instance.init_app()
connect.init_app(app=app, database=db)


@app.post("/{bot_name}", status_code=201, response_description="New Request")
async def root(bot_name: str, telegram: RequestTelegramWebhook):
    """Endpoint root for receiving request"""
    return await new_message(telegram=telegram, db=db)

