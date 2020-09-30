from app.database.model.model import telegram_from, telegram_chat, telegram_messages
from databases import Database
from typing import Union, Any
from sqlalchemy.sql.expression import ClauseElement
from pydantic import BaseModel
from app.schema import RequestTelegramWebhook
from sqlalchemy import Table
from datetime import datetime


def create_datetime() -> dict:
    dt = datetime.now()
    return {"created_at": dt, "updated_at": dt}


async def insert(table: Table, values: dict, db: Database) -> int:
    query = table.insert().values({**values, **create_datetime()})
    await db.execute(query=query)
    return values["id"]


async def update(table: Table, model: BaseModel, db: Database) -> int:
    query = (
        table.update()
        .where(table.c.id == model.id)
        .values({**model.dict(), "updated_at": create_datetime()["updated_at"]})
    )
    await db.execute(query=query)
    return model.id


async def select(table: Table, model: BaseModel, db: Database, id: int = None) -> dict:
    if not id:
        id = model.id
    query = table.select(table.c.id == id)
    return await db.fetch_one(query=query)


async def new_message(telegram: RequestTelegramWebhook, db: Database) -> dict:
    message = telegram.message
    result_from = await select(table=telegram_from, model=message.from_, db=db)
    result_chat = await select(table=telegram_chat, model=message.chat, db=db)
    result_message = await select(table=telegram_messages, model=None, db=db, id=telegram.update_id)

    if result_message:
        return telegram.dict()

    if not result_from:
        id_from = await insert(table=telegram_from, values=message.from_.dict(), db=db)
    else:
        id_from = await update(table=telegram_from, model=message.from_, db=db)

    if not result_chat:
        id_chat = await insert(table=telegram_chat, values=message.chat.dict(), db=db)
    else:
        id_chat = await update(table=telegram_chat, model=message.chat, db=db)
    
    entities = message.entities[0].dict() if message.entities else {}
    message_values = {
        "id": telegram.update_id,
        "message_id": message.message_id,
        "from_id_fk": id_from,
        "chat_id_fk": id_chat,
        **create_datetime(),
        **entities,
        **telegram.message.dict(exclude={"from_", "chat", "entities", "message_id"}),
    }
    await insert(table=telegram_messages, values=message_values, db=db)

    return telegram.dict()
