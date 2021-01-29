import logging
import settings
from telegram.ext import Updater , CommandHandler , MessageHandler, Filters
from add_user_from_bot import new_user_from_bot
from get_data import best_book_for_you
from models import User
import random
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
            user_name = user_page[4]
            
        elif 'reader' in user_page: 
            user_name = user_page[2]    
            
        context.user_data['user_name'] = user_name
        old_user = User.query.filter(User.name == user_name).first()
        if old_user == None:
            update.message.reply_text('Я пока о тебе ничего не знаю, придется немного подождать ....')
            new_user_from_bot(user_name)
            answer = best_book_for_you(user_name)
            your_five_book(update , answer)

        else : 
            answer = best_book_for_you(user_name)
            your_five_book(update , answer)
    else:
        update.message.reply_text("Что то пошло не так. Видимо не тот сайт")


def your_five_book(update , answer):
    x = 0
    leght_list = len(answer)
    while x < leght_list:
        x += 1
        random_numb = random.randint(0 , leght_list)
        update.message.reply_text(answer[random_numb])
        if x == 5:
            x = leght_list 

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", start))    
    dp.add_handler(MessageHandler(Filters.text, user_name_livelib))
    mybot.start_polling()
    mybot.idle()
    
if __name__ == "__main__":
    main()