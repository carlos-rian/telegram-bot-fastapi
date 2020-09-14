from fastapi import FastAPI

from app.schema_api import RequestTelegramWebhook, ResponseTelegramWebhook
from app.database_api import instance_db
from app.database_api import connect_db
from app.database_api import model_db
from app.database_api.model_db.model import telegram_from, telegram_chat, telegram_messages


app = FastAPI(title="Telegram Async - Fast Api")

model_db.init_app()
db = instance_db.init_app()
connect_db.init_app(app=app, database=db)


@app.post("/", response_model=ResponseTelegramWebhook, status_code=201)
async def read_root(telegram: RequestTelegramWebhook):
    # TODO
    query_from = telegram_from.insert().values(telegram.message.from_.dict())
    await db.execute(query=query_from)
    return {"Message": "World"}

