# -*- coding: utf-8 -*-
import requests
import time
from fake_useragent import UserAgent
from    hederres_const  import  const_headerrs,  cconst_nacchalo_zagotov,cconst_end_zagotov
from bs4 import BeautifulSoup

from  models  import  Book,User,Review,NoResultFound,IntegrityError
from db import db_session
import    random
jar = requests.cookies.RequestsCookieJar()
def get_html(URL):
    try:
        response  =requests.get(URL)
        response.encoding = 'utf-8'

        jar = response.cookies
        headerss=const_headerrs

        rq  = requests.post(URL , cookies=jar,headers=headerss)
        rq.encoding = 'utf-8'

        time.sleep(random.randint(40, 45))
        return  rq.text
    except(requests.RequestException,ValueError):
        return False


def find_flag_next(html):#  находим ссылкку  на  сследующие  страницу
    soup = BeautifulSoup(html , 'html.parser')

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

def  get_or_create_book(id__livelib,name_book):
    c=  Book.query.filter(Book.livelib_id == id__livelib).first()
    if    not  c  :
        c = Book()
        c.name = name_book
        c.id__livelib = id__livelib
        db_session.add(c)
        db_session.commit()

    return  c

def get_or_create_user(username):
    user = User.query.filter(User.name == username).first()
    if not user:
        user = User(name = username)
        db_session.add(user)
        db_session.commit()
    return user

# всставиить  условие  проверкки  для  Rreviewer
#def  get_orr_rreviewer(user_name,reviewer_name):
   # if Review.query.filter(Review.id == reviewer_name.id).count() ==0  and


    #try:
        #pass
        #c1=Review.query.filter(Review.user_id == user.id).one()
    #except NoResultFound:
        #

    #pass
def  funncct_get_db(name_book,id__livelib,reviewer_name,score):

    book=get_or_create_book(id__livelib,name_book)


    user= get_or_create_user(reviewer_name) #User.query.filter(User.name == name_2).one()  #session.query(Author).filter(Author.name_2 == name_2  ).one()

    s = Review()
    s.score=score
    user.reviews.append(s)
    s.book=book
    #s.books.append(book)
    db_session.add(s)
    db_session.add(user)
    db_session.commit()


def  func_add_bc(id_name):
    strig_bbufer=cconst_nacchalo_zagotov+str(id_name)
    i=0
    flag=True
    print('strig_bbufer=',strig_bbufer)
    html=get_html(strig_bbufer)
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
                funncct_get_db(book__namerr , id__livelib2 ,  athor ,  nummb)



        else:
            athor_recendent,athor_recendent_nummber =find_all_name_all_big(html)
            for athor,nummb in  zip(athor_recendent,athor_recendent_nummbers):
                funncct_get_db(book__namerr , id__livelib2 ,  athor ,  nummb)



        next=find_flag_next(html)

        if  next==''  or  i==6:

            db_session.commit()
            break
        #time.sleep(random.randint(7, 30))
        bufer_nachalo_poisk=cconst_nacchalo_zagotov+str(next)
        html=get_html(bufer_nachalo_poisk)
