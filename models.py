from sqlalchemy import Column, Integer, String
from db import Base, engine

class User(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    book_name = Column(String , unique=True)
    book_livelib_id = Column(String , unique=True)


    def __repr__(self):
        return f'<Book {self.book_name} {self.book_livelib_id}>'

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String , unique=True)

    def __repr__(self):
        return f'<User {self.user_name}>'

        
class User(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer)
    score = Column(Integer)
    author_id = Column(String)
    
    def __repr__(self):
        return f'<Book {self.book_name} {self.book_livelib_id}>'

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)