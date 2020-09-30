from pydantic import BaseModel
from typing import Dict


class ResponseTelegramWebhook(BaseModel):
    """Map response to telegram

    Args:
        BaseModel ([type]): Inherit from pydantic
    """

    message: str
