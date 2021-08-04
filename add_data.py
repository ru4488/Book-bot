from db import db_session
from models import User, Review, Book, Used_User
from  func_cicle  import  func_add_bc

from sqlalchemy import Column, Integer, String, and_
from sqlalchemy.orm.exc import NoResultFound


def store_books(all_info):
    user = get_or_create_user(all_info[0]['user'])
    review_list = []
    for row in all_info:
        
        book = get_or_create_book(row)
        review_dict = create_or_not_review(book , user, row)
        if review_dict:
            review_list.append(review_dict)
    add_all_rewiew(review_list)
  
def add_all_rewiew(review_list):
    db_session.bulk_insert_mappings(Review, review_list)
    db_session.commit()

def get_or_create_user(username):
    user = User.query.filter(User.name == username).first()
    if not user:
        user = User(
            name = username
         )

        db_session.add(user)
        db_session.commit()
    return user
  

def  Reviewers_add_db(all_info):
    for row in all_info:

        a = str(row['Url'])
        func_add_bc(a)

def get_or_create_book(row):
    book = Book.query.filter(Book.livelib_id == row['book_id']).first()
    if not book:
        book = Book(
                name=row['title'],
                livelib_id=row['book_id'],
                author=row['artist']
            )
        db_session.add(book)
        db_session.commit()
    return book

def create_or_not_review(book , user , row):
    if Review.query.filter(and_(Review.book_id == book.id , Review.user_id == user.id)).count() == 0:

        review_dict = {"user_id" : user.id,
            "score" : row['score'],
            "book_id" : book.id
        }
        return review_dict
          
        

if __name__ == "__main__":
    url = "https://www.livelib.ru/reader/LushbaughPizzicato/read"

    store_books(all_info)
    # # """поиск пользователей по книгам Вартан"""
    # Reviewers_add_db(all_info)    



'https://www.livelib.ru/reader/Tin-tinka/read'
    
'https://www.livelib.ru/reader/IrinaLinkyavichene/read'
'https://www.livelib.ru/reader/LushbaughPizzicato/read'
'https://www.livelib.ru/reader/livjuly/read'
"https://www.livelib.ru/reader/VartanPopov/read"

'https://www.livelib.ru/reader/kira_katz/read'

'https://www.livelib.ru/reader/NatalyaMayak/read'
