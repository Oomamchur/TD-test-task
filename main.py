import telegram
from fastapi import FastAPI

from schemas import TelegramMessageBase

app = FastAPI()


@app.post("/")
async def send_message(message: TelegramMessageBase) -> dict:
    try:
        bot = telegram.Bot(token=message.bottoken)
        await bot.send_message(chat_id=message.chatid, text=message.message)

        return {"Message_send": message.message}

    except Exception as e:
        return {"Check your post request": f"{type(e).__name__}: {str(e)}"}
