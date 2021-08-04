from sqlalchemy import Column, Integer, String, and_
from sqlalchemy.orm.exc import NoResultFound
from db import db_session
from models import User , Review , Book
from all_user_pages import all_page_rewiews


# соответствует ли количесвто прочтенных книг с количесвтом записанных книг в db


def how_much_books_in_db():
    users = User.query.filter(User.how_much_read != None).all()
    counting = 0
    for row in users:
        added_books = Review.query.filter(Review.user_id == row.id).count()
        print(row.id)
        if added_books < row.how_much_read:
            print(added_books , row.id)
            
            username = row.name
            user_id = row.id

            str_url = creating_url(username)
            all_page_rewiews(str_url , user_id)            

            counting += 1
            print("counting = " ,  counting)



#создаем str url   
def creating_url(username):
    url = "https://www.livelib.ru/reader/" + username + "/read~"
    return url




    

if __name__ == "__main__":
    # how_much_books_in_db()
    # url = "https://www.livelib.ru/reader/Lisari/read/listview/smalllist/~"
    # information_in_html(url)    
    how_much_books_in_db()
