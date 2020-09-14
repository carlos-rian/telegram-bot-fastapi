from pydantic import BaseModel


class ResponseTelegramWebhook(BaseModel):
    """Map response to telegram

    Args:
        BaseModel ([type]): Inherit from pydantic
    """

    message: str
