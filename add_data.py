from db import db_session
from models import User, Review, Book
from my_page_book import all_page_info
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm.exc import NoResultFound
from  func_cicle  import  func_add_bc

def store_books(all_info):
    for row in all_info:
        #print('row=',row)
        if not Book.query.filter(Book.livelib_id == row['book_id']).first():
            user = get_or_create_user(row['user'])

            book = Book(
                name=row['title'],
                livelib_id=row['book_id'],
                author=row['artist']
            )
            db_session.add(book)
            db_session.commit()

            review = Review(
                user_id=user.id,
                score=row['score'],
                book_id=book.id
            )

            db_session.add(review)
            db_session.commit()


def get_or_create_user(username):
    user = User.query.filter(User.name == username).first()
    if not user:
        user = User(name = username)
        db_session.add(user)
        db_session.commit()
    return user

def  Reviewers_add_db(all_info):
    for row in all_info:

        a=str(row['Url'])
        func_add_bc(a)

if __name__ == "__main__":
    #all_info = all_page_info('https://www.livelib.ru/reader/LushbaughPizzicato/read')
    all_info = all_page_info('https://www.livelib.ru/reader/lustdevildoll/read')
    store_books(all_info)
    Reviewers_add_db(all_info)
