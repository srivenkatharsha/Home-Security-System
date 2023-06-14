from telegram.ext import ApplicationBuilder
import asyncio
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()


now = datetime.now()
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("SYSTEM_OWNER_TELEGRAM_ID")

async def send_photo(chat, path,caption):
    application = ApplicationBuilder().token(TOKEN).build()
    await application.bot.sendPhoto(chat, path,caption = caption)
def procedure():
    asyncio.run(send_photo(CHAT_ID,"Unknown/Unknown.PNG", caption="Suspect photo , server time: " +now.strftime("%d/%m/%Y %H:%M:%S")))

if __name__ == '__main__':
    procedure()
