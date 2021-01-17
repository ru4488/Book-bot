from sqlalchemy import Column, Integer, String, ForeignKey, create_engine,Float,DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError

engine = create_engine('sqlite:///db_bd_bbook_athor.sqlite', echo=True)
Base = declarative_base()
class Book(Base):
    __tablename__ = "books"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    id__livelib=Column(String, unique=True)
    book_for_reviews = relationship("Review")

    def __repr__(self):
        return "<Books(name='%s')>" % self.name


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer,primary_key=True)
    name_2 = Column(String, unique=True)
    service = relationship("Review")

    def __repr__(self):
        return "<Authors(name='%s'  ')>"  %  (self.name_2)


class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer,primary_key=True)
    score=Column(DECIMAL)
    books_id = Column(Integer,ForeignKey("books.id"))
    authors_id = Column(Integer,ForeignKey("authors.id"))

    books = relationship("Book")
    authors = relationship("Author")
    def __repr__(self):
        return "<(score='%s'  ')>"  %  (self.score)


Base.metadata.create_all(engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
