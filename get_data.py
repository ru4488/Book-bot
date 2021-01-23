from models import User, Review, Book
from sqlalchemy import and_

def all_score_book(my_book):
    scores_list = []
    all_score_book = Review.query.filter(Review.book_id == my_book.id )
    for row in all_score_book:
        scores_list.append(row)
    return scores_list

def all_score_user(my_name):
    scores_list = []
    all_score_user = Review.query.filter(Review.user_id == my_name.id )
    for row in all_score_user:
        scores_list.append(row)
    return scores_list


def all_books_user(my_name , my_book):
    all_books_user_list = []
    books_user = Review.query.filter(Review.user_id == my_name.id , Review.book_id == my_book.id).first()
    all_books_user_list.append(books_user)
    return all_books_user_list

# users_list = []
# my_name = User.query.filter(User.name == "LushbaughPizzicato").first() 
# books_dir = {}      
# my_book =  Book.query.filter(Book.livelib_id  == '1000330921').first()
# about_my_book = Review.query.filter(and_(Review.book_id == my_book.id , Review.user_id == my_name.id)).first()
# users_read_my_book = Review.query.filter(and_(Review.book_id == my_book.id , Review.score == about_my_book.score , Review.user_id != my_name.id)).all()

# for row in users_read_my_book:
#     users_list.append(row.user)

# books_dir[my_book] = users_list
# print(books_dir)

book_score_dir = {}
my_book =  Book.query.first()
book_scores = all_score_book(my_book)
book_score_dir[my_book] = book_scores
# print(book_score_dir)

user_score_dir = {}
my_name = User.query.filter(User.name == "LushbaughPizzicato").first()
user_score = all_score_user(my_name)
user_score_dir[my_name] = user_score
# print(user_score_dir)

user_books_and_score_dir = {}
user_books_and_score = all_books_user(my_name , my_book)
user_books_and_score_dir[my_name] = user_books_and_score
print(user_books_and_score_dir)




