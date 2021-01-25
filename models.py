from sqlalchemy import Column, Integer, String , DECIMAL , ForeignKey
from sqlalchemy.orm import relationship
from db import Base, engine
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError

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
    
    @classmethod
    def all_by_book(cls, book_id):
        return cls.query.filter(cls.book_id == book_id).all()
    @classmethod
    def all_by_user(cls, user_name):
        return cls.query.filter(cls.user_id == user_name).all()
    @classmethod
    def user_and_book(cls, user_name , book):
            return cls.query.filter(cls.user_id == user_name.id , cls.book_id == book.id).first()

    def __repr__(self):
        return f'<Book review {self.book_id} {self.score} {self.user} >'

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
