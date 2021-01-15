from sqlalchemy import Column, Integer, String , DECIMAL , ForeignKey
from sqlalchemy.orm import relationship
from db import Base, engine

class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    book_name = Column(String)
    book_livelib_id = Column(String , unique=True)
    book_author =  Column(String)
    book_for_reviews = relationship("Reviews")

    def __repr__(self):
        return f'<Book {self.book_name} {self.book_livelib_id} {self.book_author}>'

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer , primary_key=True)
    user_name = Column(String , unique=True )
    user_for_reviews = relationship("Reviews")

    def __repr__(self):
        return f'<User {self.user_name}>'

        
class Reviews(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer , ForeignKey('books.id'))
    score = Column(DECIMAL)
    user_id = Column(Integer , ForeignKey('users.id'))
    
    
    def __repr__(self):
        return f'<Book review {self.book_id} {self.score} {self.author_id} >'

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)