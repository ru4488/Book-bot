from db import db_session
from models import User, Review, Book, Used_User
from my_page_book import all_page_info , how_many_books
from  func_cicle  import  func_add_bc

from sqlalchemy import Column, Integer, String, and_
from sqlalchemy.orm.exc import NoResultFound


def store_books(all_info):
    for row in all_info:
        user = get_or_create_user(row['user'])
        book = get_or_create_book(row)
        create_or_not_review(book , user, row)
        old_old_user(row['user'])



def get_or_create_user(username):
    user = User.query.filter(User.name == username).first()
    if not user:
        user = User(name = username)
        db_session.add(user)
        db_session.commit()
    return user
# "Добавляет пользователя у которого взяли информацию про все его книги"
def old_old_user(username):
    used_user = Used_User.query.filter(Used_User.name == username).first()
    if not used_user:
        used_user = Used_User(name = username)
        db_session.add(used_user)
        db_session.commit()    

def  Reviewers_add_db(all_info):
    for row in all_info:

        a=str(row['Url'])
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
        review = Review(
            user_id=user.id,
            score=row['score'],
            book_id=book.id
            )

        db_session.add(review)
        db_session.commit()

# "Вставляет пользователя у которого еще не вытащили всю информацию"
def get_new_user_info(old_user):
    get_info_user = User.query.all()
    used_user_list = make_used_user_list(old_user)
    for row in get_info_user:
        if row.name not in used_user_list:
            url = 'https://www.livelib.ru/reader/' + row.name + '/read'
            all_info, =  all_page_info(url)
            store_books(all_info)
            # Reviewers_add_db(all_info)

# "Массив пользователей у которых вытащили все книги"
def make_used_user_list(old_user):
    used_user_list = []
    for row in old_user:
        if row not in used_user_list:
            used_user_list.append(row.name)
    return used_user_list
        
    

if __name__ == "__main__":
    # url = 'https://www.livelib.ru/reader/VartanPopov/read'
    # all_info = all_page_info(url)
    store_books(all_info)
    # # """поиск пользователей по книгам Вартан"""
    # Reviewers_add_db(all_info)    
    
    'собирать информацию по новым пользователям'
    old_user = Used_User.query.all()
    get_new_user_info(old_user)

    
'https://www.livelib.ru/reader/Anton-Kozlov/read'
'https://www.livelib.ru/reader/LushbaughPizzicato/read'
'https://www.livelib.ru/reader/livjuly/read'
"https://www.livelib.ru/reader/VartanPopov/read"

'https://www.livelib.ru/reader/kira_katz/read'

'https://www.livelib.ru/reader/NatalyaMayak/read'
