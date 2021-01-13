from db import db_session
from models import Users , Reviews , Books
from my_page_book import all_page_info
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm.exc import NoResultFound
# from db import db_session


all_info = all_page_info('https://www.livelib.ru/reader/LushbaughPizzicato/read')
for user_for_the_table in range(len(all_info)):
    
    new_user = all_info[user_for_the_table]['user']
    try:
        Users.query.filter(Users.user_name == new_user).one()
    except NoResultFound:
        add_user = Users(user_name = new_user)
        db_session.add(add_user)
        db_session.commit()

    
    new_book_name = all_info[user_for_the_table]['title']
    new_livelib_id = all_info[user_for_the_table]['book_id']
    new_book_author = all_info[user_for_the_table]['artist'] 
    try:
        Books.query.filter(Books.book_livelib_id == new_livelib_id).one()
    except NoResultFound:
        add_books = Books(book_name = new_book_name , book_livelib_id = new_livelib_id , book_author = new_book_author) 
        db_session.add(add_books)
        db_session.commit()
          
# # 
# # if new_livelib_id not in all_about_books:


# Users.query.order_by(user.id)

# print(Books.query.one())
# for i in Books.query.order_by(Books.id):
#     print(i.book_livelib_id)
#     for instance in session.query(User).order_by(User.id):
# ...     print(instance.name, instance.fullname)

# my_user = Users.query.all()
# print(my_user[0].user_name)




