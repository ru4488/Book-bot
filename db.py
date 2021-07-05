from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import settings

# engine = create_engine(settings.password_cxbsnnoh)
#engine = create_engine('sqlite:///db_bd_bbook_athor.sqlite', echo=True)
# db_session = scoped_session(sessionmaker(bind=engine))

engine = create_engine(settings.password_localhost)
db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
