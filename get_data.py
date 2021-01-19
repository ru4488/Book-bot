from models import User, Review, Book

all_4 = Review.query.filter(Review.score.in_([0 , 4])).all()
book_with_score = []
# for row in all_4:
# book_with_4 = Book.query.filter(Book.id.in_(all_4))
    # book_with_score.append(book_with_4) 
print(all_4)







