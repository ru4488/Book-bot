from sqlalchemy import Column, Integer, String , DECIMAL , ForeignKey
from sqlalchemy.orm import relationship
from db import Base, engine

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    livelib_id = Column(String , unique=True)
    author =  Column(String)
    reviews = relationship("Review", back_populates="book" )

    def __repr__(self):
        return f'<Book {self.name} {self.livelib_id} {self.author}>'

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer , primary_key=True)
    name = Column(String , unique=True )
    reviews = relationship("Review" , back_populates="user")

    def __repr__(self):
        return f'<User {self.name}>'

        
class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer , ForeignKey('books.id'))
    user = relationship("User" , back_populates="reviews" )
    book = relationship("Book", back_populates="reviews")
    score = Column(DECIMAL)
    user_id = Column(Integer , ForeignKey('users.id'))
    
    
    def __repr__(self):
        return f'<Book review {self.book_id} {self.score} {self.user} >'

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)