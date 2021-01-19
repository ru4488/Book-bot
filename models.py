from sqlalchemy import Column, Integer, String , DECIMAL , ForeignKey
from sqlalchemy.orm import relationship
from db import Base, engine

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    livelib_id = Column(String , unique=True)
    author =  Column(String)
    review = relationship("Review" , backref="books" )

    def __repr__(self):
        return f'<Book {self.name} {self.livelib_id} {self.author}>'

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer , primary_key=True)
    name = Column(String , unique=True )
    review = relationship("Review" , backref="users")

    def __repr__(self):
        return f'<User {self.name}>'

        
class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer , ForeignKey('books.id'))
    user = relationship("User" , backref="reviews" )
    book = relationship("Book" , backref="reviews")
    score = Column(DECIMAL)
    user_id = Column(Integer , ForeignKey('users.id'))
    
    
    def __repr__(self):
        return f'<Book review {self.book_id} {self.score} {self.user_id} >'

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)