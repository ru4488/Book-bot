from models import User, Review, Book
from sqlalchemy import and_
from collections import Counter


def reviews_like_mine(user , all_by_user):
    reviews_like_mine_list = []
    for row in all_by_user:
        same_reviews = Review.query.filter(Review.book_id == row.book_id,
                                   Review.user_id != user.id , 
                                   Review.score == row.score
                                    ).all()
        if len(same_reviews) != 0:
            reviews_like_mine_list += same_reviews
         
    return reviews_like_mine_list


def most_simular_user_ids(reviews_like_mine_list):
    user_like_me_count_list = []
    for row in  reviews_like_mine_list:
        user_like_me_count_list.append(row.user_id)

    most_user = []
    three_most_user = Counter(user_like_me_count_list).most_common(3)

    for row in three_most_user:
        # if row[1] > 3:
        most_user.append(row[0])

    return most_user

def get_book(most_user):
    best_book_list = []
    best_books_id = []
    for row in most_user:
        best_book = Review.query.filter(Review.user_id == row , Review.score >= 4 ).all()
        best_book_list += best_book
    for i in best_book_list:
        if i.book_id not in best_books_id:
            best_books_id.append(i.book_id)
  
    return best_books_id

# book =  Book.query.first()
# all_by_book = Review.all_by_book(book.id)
# # my_book.reviews
# print(all_by_book)
def remove_the_read_ones(best_book_id , user):
    user_book = Review.query.filter(Review.user_id == user.id).all()
    for row in user_book:
        if row.book_id in best_book_id: 
            best_book_id.remove(row.book_id)
    book_for_you_list = []
    for i in best_book_id:
        
        book_for_you =  Book.query.filter(Book.id == i).first()
        book_for_you_list.append(f'{book_for_you.name} - {book_for_you.author}' )
    print(book_for_you_list)



def best_book_for_you(name):
    user = User.query.filter(User.name == name).first()
    all_by_user = Review.all_by_user(user.id)

    reviews_like_mine_list = reviews_like_mine(user , all_by_user)
    most_user = most_simular_user_ids(reviews_like_mine_list)
    best_book_id = get_book(most_user)
    remove_the_read_ones(best_book_id , user)
    

# user_book_info = Review.user_and_book(user_name , book)

if __name__ == "__main__":
    name = "VartanPopov"
    best_book_for_you(name)

# "https://www.livelib.ru/reader/VartanPopov/read"
    
    













