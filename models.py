from sqlalchemy import Column, Integer, String , DECIMAL , ForeignKey
from sqlalchemy.orm import relationship
from db import Base, engine

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    livelib_id = Column(String , unique=True)
    author =  Column(String)
    reviews = relationship("Review", backref="reviews")

    def __repr__(self):
        return f'<Book {self.book_name} {self.book_livelib_id} {self.book_author}>'

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer , primary_key=True)
    name = Column(String , unique=True )
    review = relationship("Review" , backref="reviews")

    def __repr__(self):
        return f'<User {self.user_name}>'

        
class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer , ForeignKey('books.id'))
    user = relationship("User" , backref="users" )
    book = relationship("Book" , backref="books")
    score = Column(DECIMAL)
    user_id = Column(Integer , ForeignKey('users.id'))
    
    
    def __repr__(self):
        return f'<Book review {self.book_id} {self.score} {self.author_id} >'

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)