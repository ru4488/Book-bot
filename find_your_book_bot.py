import logging
import settings
from telegram.ext import Updater , CommandHandler , MessageHandler, Filters

logging.basicConfig(filename='bot.log', level=logging.INFO)

def start(update, context):
    if 'id' not in context.user_data:
        context.user_data['id'] = update.message.chat.id
        update.message.reply_text('Привет, дорогой друг! Присылай свою страницу с прочитанными книгами с сайта https://www.livelib.ru/')
    update.message.reply_text('Я тебя помню')
    
    

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", start))    
    # dp.add_handler(MessageHandler(Filters.text, your_book))
    mybot.start_polling()
    mybot.idle()
    
if __name__ == "__main__":
    main()