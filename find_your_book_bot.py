import logging
import settings
from telegram.ext import Updater , CommandHandler , MessageHandler, Filters
from add_user_from_bot import new_user_from_bot
from get_data import best_book_for_you
from models import User
logging.basicConfig(filename='bot.log', level=logging.INFO)


def start(update, context):
    if 'id' in context.user_data:
        update.message.reply_text('Я тебя помню.')
    else:
        context.user_data['id'] = update.message.chat.id
        update.message.reply_text('Привет, дорогой друг! Присылай свою страницу с прочитанными книгами с сайта https://www.livelib.ru/')

def user_name_livelib(update, context):
    user_page = (update.message.text).split('/')

    if "www.livelib.ru" in user_page:
        if ('https:' in user_page) and ('reader' in user_page):
            context.user_data['user_name'] = user_page[4]
            old_user = User.query.filter(User.name == user_page[4]).first()
            if old_user == None:
                update.message.reply_text('Я пока о тебе ничего не знаю, придется немного подождать ....')
                new_user_from_bot(user_page[4])
            else: 
                best_book_for_you(user_page[4])

                
        elif 'reader' in user_page:
            context.user_data['user_name'] = user_page[2]
            old_user = User.query.filter(User.name == user_page[4]).first()
            new_user_from_bot(user_page[4])
            update.message.reply_text(user_page[2])
            if old_user == None:
                update.message.reply_text('Я пока о тебе ничего не знаю, придется немного подождать ....')
                new_user_from_bot(user_page[4])
            else: 
                best_book_for_you(user_page[4])
        else:
            update.message.reply_text("Не могу тебя распознать. Убедись, что в ссылке есть твой никнейм")  
    else:
        update.message.reply_text("Что то пошло не так. Видимо не тот сайт")


def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", start))    
    dp.add_handler(MessageHandler(Filters.text, user_name_livelib))
    mybot.start_polling()
    mybot.idle()
    
if __name__ == "__main__":
    main()