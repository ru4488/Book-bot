# -*- coding: utf-8 -*-
import requests
import time
from fake_useragent import UserAgent
from    hederres_const  import  const_headerrs,  cconst_nacchalo_zagotov
from bs4 import BeautifulSoup

from  models  import  Book,Author,Review,session,NoResultFound,IntegrityError

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

        tetle3=(str(recen__iter.get_text).split()[6])
        recenzia_numbers.append((tetle3))
    return  recendents  ,  recenzia_numbers


def  funncct_get(name_book,id__livelib,name_2,score):
    i=0


    try:

        c1=  session.query(Book).filter(Book.name == name_book  ).one()
    except NoResultFound:
        i=i+1
        c = Book()
        c.name = name_book
        c.id__livelib = id__livelib

        session.add(c)

    else:
        c2=  session.query(Book).filter(Book.id__livelib == id__livelib  ).first()

    if  i==1:
            try:
                p1=  session.query(Author).filter(Author.name_2 == name_2  ).one()
            except NoResultFound:
                p = Author()
                p.name_2 = name_2
                session.add(p)
                s = Review()
                s.score=score
                p.service.append(s)
                s.books=c
                session.add(s)
                session.add(p)
            else:
                p2=  session.query(Author).filter(Author.name_2 == name_2  ).first()
                s2=  session.query(Review).filter(Review.score == score  ).first()
                session.add(c)
                session.add(p2)
                p2.service.append(s)
                s2.books=c
                session.add(s2)
                session.add(p2)
    else:
        c2=  session.query(Book).filter(Book.id__livelib == id__livelib  ).first()
        session.add(c2)
        try:
            p1=  session.query(Author).filter(Author.name_2 == name_2  ).one()
        except NoResultFound:
            p = Author()
            p.name_2 = name_2
            session.add(p)
            s = Review()
            s.score=score
            p.service.append(s)
            s.books=c2
            session.add(s)
            session.add(p)
        else:
            p2=  session.query(Author).filter(Author.name_2 == name_2  ).first()
            s2=  session.query(Review).filter(Review.score == score  ).first()
            session.add(c2)
            session.add(p2)
            #s = Review()
            #s.score=score
            p2.service.append(s2)
            s2.books=c2
            session.add(s2)
            session.add(p2)


    session.commit()


#def  func_add_bc(id_name):  #
if __name__ =='__main__':
    i=0
    flag=True
    #ferr=[1005455629,]
    #strig_bbufer='https://www.livelib.ru/book/'+str(id_name)+'#reviews'
    strringerr=['https://www.livelib.ru/book/1005455629#reviews','https://www.livelib.ru/book/1002953903#reviews']


    for buferr_adres__html  in  strringerr:
        #i=0
        i=0
        flag=True
        html=get_html(buferr_adres__html)


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

                athor_recendent,athor_recendent_nummbers= find_all_name_all_big(html)
                book__namerr=str(buferr_book[0])



                for athor,nummb in  zip(athor_recendent,athor_recendent_nummbers):
                    funncct_get(book__namerr , id__livelib2 ,  athor ,  nummb)



            else:
                athor_recendent,athor_recendent_nummber =find_all_name_all_big(html)
                for athor,nummb in  zip(athor_recendent,athor_recendent_nummbers):
                    funncct_get(book__namerr , id__livelib2 ,  athor ,  nummb)



            next=find_flag_next(html)

            if  next=='':

                session.commit()
                break

            bufer_nachalo_poisk=cconst_nacchalo_zagotov+str(next)
            html=get_html(bufer_nachalo_poisk)
