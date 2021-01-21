from models import User, Review, Book
from sqlalchemy import and_


users_list = []
my_name = User.query.filter(User.name == "LushbaughPizzicato").first() 
books_dir = {}      
my_book =  Book.query.filter(Book.livelib_id  == '1000330921').first()
books_dir[my_book.id] = ''
about_my_book = Review.query.filter(and_(Review.book_id == my_book.id , Review.user_id == my_name.id)).first()
users_read_my_book = Review.query.filter(and_(Review.book_id == my_book.id , Review.score == about_my_book.score , Review.user_id != my_name.id)).all()

for row in users_read_my_book:

    users_list.append(row.user_id)
books_dir[my_book.id] = users_list
print(books_dir)










# books_dir = {}
# books_list = []
# my_name = User.query.filter(User.name == "LushbaughPizzicato").first() 
# my_book = Review.query.filter(Review.user_id == my_name.id)
# for row in my_book:
#     all_score = Review.query.filter(and_(Review.score == row.score , Review.book_id == row.book_id , Review.user_id != my_name.id))
#     books_dir = {}
#     for i in all_score:
       
#         books_dir[i.book_id] = i.user_id
#         books_list.append(books_dir)
# print(books_list)
    