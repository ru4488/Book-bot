from sqlalchemy import Column, Integer, String, and_
from sqlalchemy.orm.exc import NoResultFound
from db import db_session
from models import User, Review, Book, Used_User

from my_page_book import all_page_info , how_many_books




def how_much_read_books(old_user):
    for row in old_user:
        print(row.name)
        user = User.query.filter(User.name == row.name).first()
        if user.how_much_read == None:
            url = 'https://www.livelib.ru/reader/' + row.name + '/read'
            all_info , much_books = all_page_info(url)
            if  much_books != 0:
                user.how_much_read = int(much_books)
                db_session.add(user)
                db_session.commit()
                print(much_books)
            else:
                user.how_much_read == 0
                db_session.add(user)
                db_session.commit()
                print(much_books)


if __name__ == "__main__":
    old_user = User.query.all()
    how_much_read_books(old_user)