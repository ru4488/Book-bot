# -*- coding: utf-8 -*-
import requests
import time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

import    random
from sqlalchemy import Table, create_engine,Column, Integer, String, MetaData, ForeignKey,select,Float
from    hederres_const  import  const_headerrs,  cconst_nacchalo_zagotov
from sqlalchemy.orm import  sessionmaker
def get_html(URL):
    try:
        response  =requests.get(URL)
        response.encoding = 'utf-8'

        jar = response.cookies
        headerss=const_headerrs

        rq  = requests.post(URL , cookies=jar,headers=headerss)
        rq.encoding = 'utf-8'

        time.sleep(random.randint(1, 30))
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
    Name_book_tag = soup.select('h1.bc__book-title')[0].text.strip()
    Name_athor_tag = soup.find_all('a',class_='bc-author__link')
    athor_name=[]
    for Na in Name_athor_tag:
         tetle=Na.text
         athor_name.append(tetle)

    return Name_book_tag,  athor_name


def find_all_name_all_big(html,rencedent,recenzia_number):
    '''находим рецендента  и его  оценку   '''
    soup=BeautifulSoup(html,'html.parser')
    name_recendent = soup.find_all('a',class_='header-card-user__name')
    recendent_number = soup.find_all('span',class_='lenta-card__mymark')


    for Na in name_recendent:
        tetle2=Na.text
        rencedent.append(tetle2)


    for Na in recendent_number:

        tetle3=float(str(Na.get_text).split()[6])
        recenzia_number.append((tetle3))




if __name__ =='__main__':
    i=0
    flag=True
    engine = create_engine('sqlite://', echo=True)
    metadata = MetaData()
    Books_table = Table('Books_id', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String)

    )

    Books_table.create(bind=engine)
    Reviewer_table = Table('Reviewer_id', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String)

    )
    Reviewer_table.create(bind=engine)

    Scores_table = Table('Scores_id', metadata,
    Column('id', Integer, primary_key=True),
    Column('reviewer_id', String,ForeignKey('Reviewer_id.name')),
    Column('book_id', String,ForeignKey('Books_id.title')),
    Column('score', Float)
    )
    Scores_table.create(bind=engine)

    Session = sessionmaker(bind=engine)
    s = Session()
    html=get_html('https://www.livelib.ru/book/1002455336/reviews#reviews')
    str_23='test'+str(i)+'.html'



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
            name_book,athor_book =find_all_name(html)
            buferr_book.append(name_book)
            buferr_book.append(athor_book)
            find_all_name_all_big(html,athor_recendent,athor_recendent_nummber)
            Books_id.append(buferr_book)
            insert_Books = Books_table.insert().values(title=buferr_book[0])
            engine.execute(insert_Books)

        else:
            find_all_name_all_big(html,athor_recendent,athor_recendent_nummber)
        for  err  in  athor_recendent:
            insert_Reviewer = Reviewer_table.insert().values(name=err)
            engine.execute(insert_Reviewer)
        for  err  in  athor_recendent_nummber:
            insert_Scoresr = Scores_table.insert().values(score=err)
            engine.execute(insert_Scoresr)
        #insert_Scoresr = Scores_table.insert().values(reviewer_id=err)


        Reviewer_id.append(athor_recendent)#  Reviewer__id


        Scores_buferr.append(Reviewer_id)
        Scores_buferr.append(Books_id)
        Scores_buferr.append(athor_recendent_nummber)
        Scores_id.append(Scores_buferr)
        if  i==2:
            meserrger1=s.query(Books_table).all()
            print('Books_id=',meserrger1)
            meserrger3=s.query(Reviewer_table).all()
            print('Reviewer_id=',meserrger3)
            meserrger=s.query(Scores_table).all()
            print('meserrger=',meserrger)
            #stmt = select([Reviewer_table.c.all])
            #message2, = engine.execute(stmt).fetchone()
            #print('message=',message2)
            break

        next=find_flag_next(html)

        if  next=='':
            break

        bufer_nachalo_poisk=cconst_nacchalo_zagotov+str(next)
        html=get_html(bufer_nachalo_poisk)
