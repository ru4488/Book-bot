from sqlalchemy import Column, Integer, String, and_
from sqlalchemy.orm.exc import NoResultFound
from db import db_session
from models import User, Review, Book, Used_User

from my_page_book import all_page_info , how_many_books
from add_data import store_books



def how_much_read_books():
    users = User.query.filter(User.how_much_read == None).all()
    for row in users:
        url = 'https://www.livelib.ru/reader/' + row.name + '/read'
        new_user = User.query.filter(User.name == row.name).first()
        
        all_info , much_books = all_page_info(url)
        if  much_books != 0:
            new_user.how_much_read = int(much_books)
            db_session.add(new_user)
            db_session.commit()
            print(much_books)
        else:
            new_user.how_much_read == 0
            db_session.add(new_user)
            db_session.commit()
            print(much_books)

def if_read_n_books():
    users = User.query.all()

    for row in users:
        a = Review.query.filter(Review.user_id == row.id).all()
        print(row.id)

        if (int(row.how_much_read) < 300) and (abs(len(a) - int(row.how_much_read)) > 5):

            url = 'https://www.livelib.ru/reader/' + row.name + '/read'
            all_info , books_read = all_page_info(url)
            store_books(all_info , books_read)


# def fact_and_theory():
#     users = User.query.all()
#     for row in users:
#         user = User.query.all(Review.user_id == row.id).first()
#         how_mach_score = Review.query.filter(Review.user_id == row.id).all()
        

    



if __name__ == "__main__":
    
    # if_read_n_books()
    # how_much_read_books()
    user = User.query.filter(User.name == "strannik102").first()
    print(user.id)