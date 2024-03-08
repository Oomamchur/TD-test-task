import telegram
from fastapi import FastAPI, HTTPException

import schemas

app = FastAPI()


@app.post("/")
async def send_message(message: schemas.TelegramMessageBase) -> dict:
    try:
        bot = telegram.Bot(token=message.bottoken)
        await bot.send_message(chat_id=message.chatid, text=message.message)

        return {"Message_send": message.message}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Check your post request: {str(e)}")
