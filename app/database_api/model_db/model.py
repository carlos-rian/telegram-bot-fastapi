from os import getenv
from datetime import datetime
from sqlalchemy import (
    Table,
    Column,
    String,
    Integer,
    BigInteger,
    DateTime,
    Boolean,
    Text,
    ForeignKeyConstraint,
    MetaData,
    create_engine,
)

metadata = MetaData()

telegram_chat = Table(
    "telegram_chat",
    metadata,
    Column("id", BigInteger, nullable=False, primary_key=True, autoincrement=False),
    Column("first_name", String, nullable=True),
    Column("last_name", String, nullable=True),
    Column("username", String, nullable=True),
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
    Column("update_id", BigInteger, nullable=False, index=True),
    Column("created_at", DateTime, default=datetime.now, nullable=False),
    Column("updated_at", DateTime, default=datetime.now, nullable=False, onupdate=datetime.now),
    Column("text", Text, nullable=False),
    Column("offset", Integer, nullable=True),
    Column("length", Integer, nullable=True),
    Column("type", String(50), nullable=True),
    Column("chat_id_fk", BigInteger, nullable=True, index=True),
    Column("from_id_fk", BigInteger, nullable=True, index=True),
    ForeignKeyConstraint(
        columns=["chat_id_fk", "from_id_fk"],
        refcolumns=["telegram_chat.id", "telegram_from.id"],
        name=["fk_messages_chat_id", "fk_messages_from_id"],
        onupdate="CASCADE",
        ondelete="SET NULL",
    ),
)
