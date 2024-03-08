from pydantic import BaseModel


class TelegramMessageBase(BaseModel):
    bottoken: str
    chatid: str
    message: str
