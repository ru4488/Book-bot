from db import db_session
from models import Users, Reviews, Books
from my_page_book import all_page_info
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm.exc import NoResultFound


def store_books(all_info):
    for row in all_info:
        if not Books.query.filter(Books.book_livelib_id == row['book_id']).first():    
            user = get_or_create_user(row['user'])

            book = Books(
                book_name=row['title'],
                book_livelib_id=row['book_id'],
                book_author=row['artist']
            )
            db_session.add(book)
            db_session.commit()

            review = Reviews(
                user_id=user.id,
                score=row['score'],
                book_id=book.id
            )

            db_session.add(review)
            db_session.commit()
        

def get_or_create_user(username):
    user = Users.query.filter(Users.user_name == username).first()
    if not user:
        user = Users(user_name = username)
        db_session.add(user)
        db_session.commit()
    return user


if __name__ == "__main__":
    all_info = all_page_info('https://www.livelib.ru/reader/kupreeva74/read')
    store_books(all_info)
