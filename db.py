from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgres://cxbsnnoh:TyklLzrRQMcP1RFgluIAMu3INmGO2O0L@hattie.db.elephantsql.com:5432/cxbsnnoh')
#engine = create_engine('postgres://qniettly:yvktFGsJHxIx3GVQ_-PiYf1NppelUvCm@hattie.db.elephantsql.com:5432/qniettly')
#engine = create_engine('sqlite:///db_bd_bbook_athor.sqlite', echo=True)
db_session = scoped_session(sessionmaker(bind=engine))
#proxiess = [
    ##"https://91.20.3.107:8085",
    #"https://91.23.94.107:8085",
    #"https://91.24.14.113:8085",
    #"https://146.15.204.70:8085",
    #"https://193.10.171.7:8085"]
#proxies = {
    #"http": 'http://209.50.52.162:9050',
    #"https": 'http://186.86.247.169'
#}
proxies = ['104.248.159.145:8888', '113.53.83.252:54356', '206.189.236.200:80', '218.48.229.173:808', '119.15.90.38:60622', '186.250.176.156:42575']
Base = declarative_base()
Base.query = db_session.query_property()
