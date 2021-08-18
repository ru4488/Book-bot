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
    ids_list = []
    for row in  reviews_like_mine_list:
        ids_list.append(row.user_id)

    three_user_ids_list = []
    three_most_ids = Counter(ids_list).most_common(3)

    for row in three_most_ids:
        # if row[1] > 3:
        three_user_ids_list.append(row[0])

    return three_user_ids_list

def get_book_ids(three_user_ids_list):
    best_books_list = []
    best_books_ids = []
    for row in three_user_ids_list:
        best_books = Review.query.filter(Review.user_id == row , Review.score >= 4 ).all()
        best_books_list += best_books

    for i in best_books_list:
        if i.book_id not in best_books_ids:
            best_books_ids.append(i.book_id)
    return best_books_ids


def remove_the_read_ones(best_books_ids , user):
    user_books = Review.query.filter(Review.user_id == user.id).all()
    for row in user_books:
        if row.book_id in best_books_ids: 
            best_books_ids.remove(row.book_id)
    best_books = Book.query.filter(Book.id.in_(best_books_ids)).all()
    
    book_for_you_list = []
    for row in best_books:
        book_for_you_list.append(f'{row.name} - {row.author}' )
    # print(book_for_you_list)
    return book_for_you_list



def best_book_for_you(name):
    user = User.query.filter(User.name == name).first()
    all_by_user = Review.all_by_user(user.id)

    reviews_like_mine_list = reviews_like_mine(user , all_by_user)
    most_user = most_simular_user_ids(reviews_like_mine_list)
    best_books_ids = get_book_ids(most_user)
    best_book_list = remove_the_read_ones(best_books_ids , user)
    return best_book_list
    

# user_book_info = Review.user_and_book(user_name , book)

if __name__ == "__main__":
    name = "LushbaughPizzicato"
    best_book_for_you(name)

# "https://www.livelib.ru/reader/VartanPopov/read"
    
    













