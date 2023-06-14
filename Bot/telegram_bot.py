import logging
import telegram
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, ContextTypes
import threading
from playsound import playsound
from dotenv import load_dotenv
import os

load_dotenv()


class TelegramBot:
    TOKEN = os.getenv("BOT_TOKEN")
    alert = False

    def __init__(self):
        logging.basicConfig (
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
        )

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "Hi there! Welcome to SentinelBot, the companion bot to your home security system | type /alarmConfig for operating the alarm system.")


    async def reply_keyboard(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        kb = [[telegram.KeyboardButton('/startAlarm')],
            [telegram.KeyboardButton('/stopAlarm')]]
        kb_markup = telegram.ReplyKeyboardMarkup(kb, resize_keyboard=True, one_time_keyboard=False)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Alright, on your command...", reply_markup=kb_markup)

    async def yes(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Alert has been sent.")
        self.alert = True
            
    async def no(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self.alert = False
        await context.bot.send_message(chat_id=update.effective_chat.id, text="The alarm has been stopped")
    
    def play_alarm(self):
        while True:
            if self.alert:
                print("playing the alarm")
                playsound(os.path.dirname(__file__) + '\\beep.mp3')

    def main(self):
        t = threading.Thread(target = self.play_alarm)
        t.daemon = True
        t.start()
        application = ApplicationBuilder().token(TelegramBot.TOKEN).build()
        start_handler = CommandHandler('start', self.start)
        reply_keyboard_handler = CommandHandler('alarmConfig', self.reply_keyboard)
        yes_handler = CommandHandler('startAlarm', self.yes)
        no_handler = CommandHandler('stopAlarm', self.no)
        application.add_handler(start_handler)
        application.add_handler(reply_keyboard_handler)
        application.add_handler(yes_handler)
        application.add_handler(no_handler)
        application.run_polling()
            

bot = TelegramBot()
bot.main()
