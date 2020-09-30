from datetime import datetime
from sqlalchemy import (
    Table,
    Column,
    String,
    Integer,
    BigInteger,
    DateTime,
    Boolean,
    Enum,
    Text,
    ForeignKey,
    ForeignKeyConstraint,
    MetaData,
    create_engine,
)


def init(metadata):
    telegram_chat = Table(
        "telegram_chat",
        metadata,
        Column("id", BigInteger, nullable=False, primary_key=True, autoincrement=False),
        Column("first_name", String(50), nullable=True),
        Column("last_name", String(100), nullable=True),
        Column("username", String(33), nullable=True),
        Column("type", String(20), nullable=True),
        Column("created_at", DateTime, default=datetime.now, nullable=False),
        Column("updated_at", DateTime, default=datetime.now, nullable=False, onupdate=datetime.now),
    )

    telegram_from = Table(
        "telegram_from",
        metadata,
        Column("id", BigInteger, nullable=False, primary_key=True, autoincrement=False),
        Column("is_bot", Boolean, nullable=False),
        Column("first_name", String(50), nullable=True),
        Column("last_name", String(50), nullable=True),
        Column("username", String(33), nullable=True),
        Column("language_code", String(50), nullable=True),
        Column("is_valid", Boolean, nullable=True, default=False),
        Column("created_at", DateTime, default=datetime.now, nullable=False),
        Column("updated_at", DateTime, default=datetime.now, nullable=False, onupdate=datetime.now),
    )

    telegram_messages = Table(
        "telegram_messages",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement=False),
        Column("message_id", BigInteger, nullable=False, index=True),
        Column("offset", Integer, nullable=True),
        Column("text", Text, nullable=False),
        Column("length", Integer, nullable=True),
        Column("type", String(50), nullable=True),
        Column("date", BigInteger, nullable=True),
        Column("chat_id_fk", BigInteger, nullable=True, index=True),
        Column("from_id_fk", BigInteger, nullable=True, index=True),
        Column("created_at", DateTime, default=datetime.now, nullable=False),
        Column("updated_at", DateTime, default=datetime.now, nullable=False, onupdate=datetime.now),
        ForeignKeyConstraint(["chat_id_fk"], ["telegram_chat.id"], name="fk_chat_messages_id"),
        ForeignKeyConstraint(["from_id_fk"], ["telegram_from.id"], name="fk_from_messages_id"),
    )
    return metadata, telegram_chat, telegram_from, telegram_messages
