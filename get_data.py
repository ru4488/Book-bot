from models import User, Review, Book
from sqlalchemy import and_

books_dir = {}
books_list = []
my_name = User.query.filter(User.name == "LushbaughPizzicato").first() 
my_book = Review.query.filter(Review.user_id == my_name.id)
for row in my_book:
    all_score = Review.query.filter(and_(Review.score == row.score , Review.book_id == row.book_id , Review.user_id != my_name.id))
    books_dir = {}
    for i in all_score:
       
        books_dir[i.book_id] = i.user_id
        books_list.append(books_dir)
print(books_list)
    


# for row in my_book:


# # my_book =  Book.query.filter(Book.livelib_id  == '1000330921').first()
#     # print(row.book_id)
#     # about_my_book = Review.query.filter(and_(Review.book_id == row.book_id , Review.user_id == my_name.id)).first()
#     # print(about_my_book)
    
#     users_read_my_book = Review.query.filter(and_(Review.book_id == row.book_id , Review.score == row.score , Review.user_id != my_name.id))
#     new_book = row.book_id
#     for i in users_read_my_book:
#         books_dir[new_book] = i
#         books_list.append(books_dir)

#     # print(users_read_my_book)
#     # users_read_my_book
# print(books_list)








