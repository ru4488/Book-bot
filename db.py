from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgres://cxbsnnoh:TyklLzrRQMcP1RFgluIAMu3INmGO2O0L@hattie.db.elephantsql.com:5432/cxbsnnoh')
#engine = create_engine('sqlite:///db_bd_bbook_athor.sqlite', echo=True)
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
