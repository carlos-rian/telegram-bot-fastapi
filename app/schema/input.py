from pydantic import BaseModel
from typing import Dict, Optional, List
from datetime import datetime


class From(BaseModel):
    """Mapping of the dict From received in the message.

    Args:
        BaseModel ([type]): Pydantic inheritance.
    """

    id: int
    is_bot: bool
    first_name: str
    last_name: str
    username: str
    language_code: Optional[str] = None


class Entities(BaseModel):
    """Mapping of the dict Etities received in the message.

    Args:
        BaseModel ([type]): Pydantic inheritance.
    """

    offset: Optional[int] = None
    length: Optional[int] = None
    type: Optional[str] = None


class Chat(BaseModel):
    """Mapping of the dict Chat received in the message.

    Args:
        BaseModel ([type]): Pydantic inheritance.
    """

    id: int
    first_name: str
    last_name: str
    username: str
    type: str


class Message(BaseModel):
    """Mapping of the dict Message received in the message, nested the message json.

    Args:
        BaseModel ([type]): Pydantic inheritance.
    """

    message_id: int
    date: int
    text: str
    from_: Optional[From] = None
    chat: Optional[Chat] = None
    entities: List[Optional[Entities]] = None

    class Config:
        # alias the "from" field.
        fields = {"from_": "from"}


class RequestTelegramWebhook(BaseModel):
    """Mapping of the dict Body received in the request, nested the message json.

    Args:
        BaseModel ([type]): Pydantic inheritance.
    """

    update_id: int
    message: Message
