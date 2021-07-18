from sqlalchemy import Column, Integer, String, and_
from sqlalchemy.orm.exc import NoResultFound
from db import db_session
from models import User , Review , Book
from my_page_book import information_in_html , all_page_rewiewss
# соответствует ли количесвто прочтенных книг с количесвтом записанных книг в db


def how_much_books_in_db():
    users = User.query.filter(User.how_much_read != None).all()
    for row in users:
        added_books = Review.query.filter(Review.user_id == row.id).count()
        counting = 1
        if added_books < row.how_much_read:
            print(added_books , row.id)
            username = row.name
            url = "https://www.livelib.ru/reader/" + row.name + "/read~9"
            
            print(url)
            all_about_book_list = information_in_html(url)
            # print(all_about_book_list)

            # if not all_about_book_list :
            #     unknown = User.query.filter(User.id == row.id).first()
            #     unknown.how_much_read = None
            #     db_session.commit()
                



    
if __name__ == "__main__":
    # how_much_books_in_db()
    url = "https://www.livelib.ru/reader/Lisari/read/listview/smalllist/~"
    # information_in_html(url)    
    all_page_rewiews(url)