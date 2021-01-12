# -*- coding: utf-8 -*-
import requests
import time
from fake_useragent import UserAgent
from    hederres_const  import  const_headerrs,  cconst_nacchalo_zagotov
from bs4 import BeautifulSoup
#from moduls__db  import get_bd__books, get_bd__Authors
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload
import    random

def get_html(URL):
    try:
        response  =requests.get(URL)
        response.encoding = 'utf-8'

        jar = response.cookies
        headerss=const_headerrs

        rq  = requests.post(URL , cookies=jar,headers=headerss)
        rq.encoding = 'utf-8'

        time.sleep(random.randint(7, 30))
        return  rq.text
    except(requests.RequestException,ValueError):
        return False


def find_flag_next(html):#  находим ссылкку  на  сследующие  страницу
    soup=BeautifulSoup(html,'html.parser')

    next_sulka = soup.find_all('a',class_='pagination__page')
    cchar_nnext=''
    for sulka  in  next_sulka:
        if  sulka.text  =='›':
            cchar_nnext=sulka['href']
    return  cchar_nnext



def find_all_name(html):# нацтти  основную  информацию  про ккнигу
    '''находим  название  ккниги  '''
    soup=BeautifulSoup(html,'html.parser')
    name_book_tag = soup.select('h1.bc__book-title')[0].text.strip()
    namber_id__livilebbs =  soup.find(class_="bc-menu__status-wrapper")
    namber_id__livilebb=namber_id__livilebbs['id'].split('-')[3]

    name_athor_tags = soup.find_all('a',class_='bc-author__link')
    athor_names=[]
    for name_tag in name_athor_tags:
         tetle=name_tag.text
         athor_names.append(tetle)

    return name_book_tag,namber_id__livilebb


def find_all_name_all_big(html):
    '''находим рецендента  и его  оценку   '''
    soup=BeautifulSoup(html,'html.parser')
    names_recendent = soup.find_all('a',class_='header-card-user__name')
    recendent_numbers = soup.find_all('span',class_='lenta-card__mymark')
    recendents=[]
    recenzia_numbers=[]

    for name_recen in names_recendent:
        tetle2=name_recen.text
        recendents.append(tetle2)


    for recen__iter in recendent_numbers:

        tetle3=float(str(recen__iter.get_text).split()[6])
        recenzia_numbers.append((tetle3))
    return  recendents  ,  recenzia_numbers





if __name__ =='__main__':
    i=0
    flag=True
    engine = create_engine('sqlite:///db_bd_bbook_athor.sqlite', echo=True)
    Base = declarative_base()
    #Base.metadata.create_all(engine)

    #html=get_html('https://www.livelib.ru/book/1002455336/reviews#reviews')
    html=get_html('https://www.livelib.ru/book/1005455629#reviews')
    str_23='test'+str(i)+'.html'
    class Book(Base):
        __tablename__ = "books"
        id = Column(Integer,primary_key=True)
        name = Column(String)
        id__livelib=Column(String)

        def __repr__(self):
            return "<Books(name='%s')>" % self.name
        #segment = Column(String)
        #service = relationship("Service")

    class Author(Base):
        __tablename__ = 'authors'
        id = Column(Integer,primary_key=True)
        name_2 = Column(String)
        service = relationship("Review")
        #reviews = Column(String)
        #image = Column(String)
        def __repr__(self):
            return "<Authors(name='%s'  ')>"  %  (self.name_2)


    class Review(Base):
        __tablename__ = 'reviews'
        id = Column(Integer,primary_key=True)
        score=Column(Float)
        books_id = Column(Integer,ForeignKey("books.id"))
        authors_id = Column(Integer,ForeignKey("authors.id"))

        books = relationship("Book")
        authors = relationship("Author")
        def __repr__(self):
            return "<(score='%s'  ')>"  %  (self.score)



    # Create all tables by issuing CREATE TABLE commands to the DB.
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    Reviewer_id=[]
    Scores_id=[]
    Books_id=[]

    while(flag):
        athor_recendent_nummber=[]
        Scores_buferr=[]
        athor_recendent=[]

        i=i+1
        if i==1:
            buferr_book=[]
            name_book,id__livelib2 =find_all_name(html)
            buferr_book.append(name_book)
            #buferr_book.append(athor_book)
            athor_recendent,athor_recendent_nummbers= find_all_name_all_big(html)
            book__namerr=str(buferr_book[0])
            ed_user=Book(name=book__namerr,id__livelib=id__livelib2)
            session.add(ed_user)
            #iterator_po_author=0
            for athor,nummb in  zip(athor_recendent,athor_recendent_nummbers):
                ath=Author(name_2=athor)
                #nummb=athor_recendent_nummbers[iterator_po_author]
                s = Review(score=nummb)
                ath.service.append(s)
                s.books=ed_user
                session.add(s)
                session.add(ath)
                #iterator_po_author=iterator_po_author+1

                #ath=Author(name_2=athor)
                #session.add(ath)
            #for athor__nnumbber in  athor_recendent_nummbers:
                #ath=Review(score=athor__nnumbber)
                #session.add(ath)

        else:
            athor_recendent,athor_recendent_nummber =find_all_name_all_big(html)
            for athor,nummb in  zip(athor_recendent,athor_recendent_nummbers):
                ath=Author(name_2=athor)
                #nummb=athor_recendent_nummbers[iterator_po_author]
                s = Review(score=nummb)
                ath.service.append(s)
                s.books=ed_user
                session.add(s)
                session.add(ath)
            #for  athor  in  athor_recendent:
                #ath=Author(name_2=athor)
                #session.add(ath)
            #for athor__nnumbber in  athor_recendent_nummbers:
                #ath=Review(score=athor__nnumbber)
                #session.add(ath)

        next=find_flag_next(html)

        if  next=='':
            #session.add(ed_user)
            session.commit()
            break

        bufer_nachalo_poisk=cconst_nacchalo_zagotov+str(next)
        html=get_html(bufer_nachalo_poisk)
