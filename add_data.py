from db import db_session
from models import Users , Reviews , Books
from my_page_book import all_page_info
from sqlalchemy import Column, Integer, String


all_info = all_page_info('https://www.livelib.ru/reader/LushbaughPizzicato/read')
for user_for_the_table in range(len(all_info)):
    
    new_user = all_info[user_for_the_table]['user']
    
    all_users_name = Users.query.all()[0].user_name
    if new_user not in all_users_name:
        add_user = Users(user_name = new_user)
        db_session.add(add_user)
        db_session.commit()
    
    new_book_name = all_info[user_for_the_table]['title']
    new_livelib_id = all_info[user_for_the_table]['book_id']
    new_book_author = all_info[user_for_the_table]['artist']
   
    all_about_books = Books.query.all()[0].book_livelib_id   
    if new_livelib_id not in all_about_books:
        add_books = Books(book_name = new_book_name , book_livelib_id = new_livelib_id , book_author = new_book_author)
    
    
        db_session.add(add_books)
        db_session.commit()



# my_user = Users.query.all()
# print(my_user[0].user_name)




