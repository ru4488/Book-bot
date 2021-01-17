from sqlalchemy import Column, Integer, String, ForeignKey, create_engine,Float,DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError

#engine = create_engine('sqlite:///db_bd_bbook_athor.sqlite', echo=True)
#Base = declarative_base()
#Base.metadata.create_all(engine)
#Session = sessionmaker()
#Session.configure(bind=engine)
#session = Session()
