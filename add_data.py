from db import db_session
from models import Users , Reviews , Books
from my_page_book import all_page_info
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm.exc import NoResultFound


all_info = all_page_info('https://www.livelib.ru/reader/LushbaughPizzicato/read')
for user_for_the_table in range(len(all_info)):
    
    new_user = all_info[user_for_the_table]['user']
    try:
        Users.query.filter(Users.user_name == new_user).one()
    except NoResultFound:
        add_user = Users(user_name = new_user)
        db_session.add(add_user)
        # db_session.commit()

    
    new_book_name = all_info[user_for_the_table]['title']
    new_livelib_id = all_info[user_for_the_table]['book_id']
    new_book_author = all_info[user_for_the_table]['artist'] 
    try:
        Books.query.filter(Books.book_livelib_id == new_livelib_id).one()
    except NoResultFound:
        add_books = Books(book_name = new_book_name , book_livelib_id = new_livelib_id , book_author = new_book_author) 
        db_session.add(add_books)
        # db_session.commit()

    
    new_book_name
    new_score = all_info[user_for_the_table]['score']
    review = Reviews(score = new_score , book_id = new_book_name , author_id = new_user)
    db_session.add(review)
    db_session.commit()
          





