import logging
import settings
from telegram.ext import Updater , CommandHandler , MessageHandler, Filters

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, дорогой друг! Присылай свою страницу с прочитанными книгами с сайта https://www.livelib.ru/')


def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))    
    mybot.start_polling()
    mybot.idle()
    

main()