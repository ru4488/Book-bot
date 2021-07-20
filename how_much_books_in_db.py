from sqlalchemy import Column, Integer, String, and_
from sqlalchemy.orm.exc import NoResultFound
from db import db_session
from models import User , Review , Book
from all_user_pages import all_page_rewiews
from add_data import store_books

# соответствует ли количесвто прочтенных книг с количесвтом записанных книг в db


def how_much_books_in_db():
    users = User.query.filter(User.how_much_read != None).all()
    for row in users:
        added_books = Review.query.filter(Review.user_id == row.id).count()

        if added_books < row.how_much_read:
            print(added_books , row.id)
            
            username = row.name
            user_id = row.id

            str_url = creating_url(username)
            all_about_book_list = all_page_rewiews(str_url)            
            add_or_not(all_about_book_list , user_id)


#создаем str url   
def creating_url(username):
    url = "https://www.livelib.ru/reader/" + username + "/read~"
    return url

# добовляем книги или пишим, что нет данных 
def add_or_not(all_about_book_list , user_id):
    if len(all_about_book_list) == 0:
        unknown = User.query.filter(User.id == user_id).first()
        unknown.how_much_read = None
        db_session.commit()
    else: 
        store_books(all_about_book_list)
    

if __name__ == "__main__":
    # how_much_books_in_db()
    # url = "https://www.livelib.ru/reader/Lisari/read/listview/smalllist/~"
    # information_in_html(url)    
    how_much_books_in_db()