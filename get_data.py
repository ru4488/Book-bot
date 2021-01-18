from models import User, Review, Book

all_4 = Review.query.filter(Review.score == 4).all()
for row in all_4:
    book_with_4 = Book.query.filter(Book.id == row.id).first()
    print(book_with_4)