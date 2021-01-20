from models import User, Review, Book



# все пользователи которые поставили 3 книжке '1000330921'
book = Book.query.filter(Book.livelib_id == '1000330921').first()
score = Review.query.filter(Review.book_id == book.id)
for row in score:
    print(row.score)
    if row.score == 3:
        print(row.user)










