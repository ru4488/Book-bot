from models import User, Review, Book
from sqlalchemy import and_
from collections import Counter

def user_like_me(user_name , all_by_user):
    user_like_me_list = []
    for row in all_by_user:
        user_like_me = Review.query.filter(Review.book_id == row.book_id,
                                   Review.user_id != user_name.id , 
                                   Review.score == row.score
                                    ).all()
        if len(user_like_me) != 0:
            user_like_me_list += user_like_me
    return user_like_me_list


def count_user(user_like_me_list):
    user_like_me_count_list = []
    for row in  user_like_me_list:
        user_like_me_count_list.append(row.user_id)
    most_user = []
    three_most_user = Counter(user_like_me_count_list).most_common(3)
    for row in three_most_user:
        if row[1] > 3:
            most_user.append(row[0])
    return most_user

def get_book(most_user):
    best_book_list = []
    for row in most_user:
        best_book = Review.query.filter(Review.user_id == row , Review.score >= 4 ).all()
        best_book_list += best_book
    return best_book_list

# book =  Book.query.first()
# all_by_book = Review.all_by_book(book.id)
# # my_book.reviews
# print(all_by_book)




# user_book_info = Review.user_and_book(user_name , book)





if __name__ == "__main__":
    user_name = User.query.filter(User.name == "LushbaughPizzicato").first()
    all_by_user = Review.all_by_user(user_name.id)

    user_like_me_list = user_like_me(user_name , all_by_user)
    most_user = count_user(user_like_me_list)
    best_book = get_book(most_user)
    print(best_book)
    












