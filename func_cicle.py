# -*- coding: utf-8 -*-
import requests
#import grequests
#import async
import asyncio #  [1]
import aiohttp
import time
#import async
from fake_useragent import UserAgent
from    hederres_const  import  const_headerrs,  cconst_nacchalo_zagotov,cconst_end_zagotov
from bs4 import BeautifulSoup
from multiprocessing  import Pool
from  models  import  Book,User,Review,NoResultFound,IntegrityError
from db import db_session,proxies
import    random
from random import choice
jar = requests.cookies.RequestsCookieJar()
id=0
def get_html(URL):
    try:
        proxy = proxies#choice(proxies)#{"https" : proxiess[id % len(proxiess)]}
        print('proxy=',proxy)

        response  =requests.get(URL, proxies=proxy)
        #response  =requests.get(URL)
        response.encoding = 'utf-8'

        jar = response.cookies
        headerss=const_headerrs

        rq  = requests.post(URL , cookies=jar,headers=headerss, proxies=proxy)
        #rq  = requests.post(URL , cookies=jar,headers=headerss)
        rq.encoding = 'utf-8'

        time.sleep(random.randint(40, 45))
        return  rq.text
    except(requests.RequestException,ValueError):
        return False

def get_html2(URL):

    #time.sleep(random.randint(40, 45))
    URRL=[]
    URRL.append(URL)
    URRL.append('https://www.livelib.ru/book/1000186331/reviews/~2#reviews')
    return  URRL

    #a1=URL.split('#')
    #i=0
    #for  i  in  range(2,3):
        #a=a1[0]+'/~'+str(i)+'#reviews'
        #URRL.append(a)
    #return URRL


    #for  ij in URRL:
        #str_23='test'+str(i)+'.html'
        #async with aiohttp.ClientSession() as session:
            #async with session.get(ij) as resp:
                #await resp.text()
                #a= resp.text()
                #with open(str_23,'w',encoding='utf8') as f:
                    #await resp.text()
                    #f.write(a)




                # print(resp.status)
                 #print(await resp.text())
                 #[4]
                #response = await resp.read()
                #print(response)
    #for ii  in  URRL:
    #print(dir(grequests))
    #rs = (grequests.get(u) for u in URRL)
    #print(grequests.map(rs))
    #for _ in range(1,3):
    #headerss = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
    #requests_ = (grequests.get(u) for u in URRL)
    #requests_.encoding = 'utf-8'
    #print('requests_=',dir(requests_))
    #grequests.map(requests_)
    #print('grequests=',dir(grequests))
    #jar = requests_.request.cookies
    #rq  = grequests.post(requests_, cookies=jar,headers=headerss)
    #grequests.map(requests_)
    #rq.request.encoding = 'utf-8'
    #return  rq.request.text

        #print('ii=',ii)


        #print('i=',i)

    #pass

def find_flag_next(soup):#  находим ссылкку  на  сследующие  страницу
    #soup = BeautifulSoup(html , 'html.parser')

    next_sulka = soup.find_all('a',class_='pagination__page')
    cchar_nnext=''
    for sulka  in  next_sulka:
        if  sulka.text  =='›':
            cchar_nnext=sulka['href']
    return  cchar_nnext



def find_all_name(soup):# нацтти  основную  информацию  про ккнигу
    '''находим  название  ккниги  '''
    #soup=BeautifulSoup(html,'html.parser')
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


    #try:
        #response  =requests.get(URL)
        #response.encoding = 'utf-8'

        #jar = response.cookies
        #headerss=const_headerrs

        #rq  = requests.post(URL , cookies=jar,headers=headerss)
        #rq.encoding = 'utf-8'

        #time.sleep(random.randint(40, 45))
        #return  rq.text
    #except(requests.RequestException,ValueError):
        #return False

def  merrge__funnc(url):
    #a=1
    a1=url.split('#')

    str_23=str(a1[1])+'.html'
    print('str_23=',str_23)
    aerrt_text=get_html(url)
    print('aerrt_text=',aerrt_text)

    with open(str_23,'w',encoding='utf8') as f:
        f.write(aerrt_text)
    #pass
def  func_add_bc(id_name):
    strig_bbufer=cconst_nacchalo_zagotov+str(id_name)
    i=0
    flag=True
    #print('strig_bbufer=',strig_bbufer)
    all_URRL=get_html2(strig_bbufer)
    print('all_URRL=',all_URRL)
    with  Pool(2) as  p:
        p.map(merrge__funnc,all_URRL)


    #html=get_html(strig_bbufer)

    #while(flag):
        #athor_recendent_nummber=[]
        #Scores_buferr=[]
        #athor_recendent=[]
        #soup=BeautifulSoup(html,'html.parser')

        #i=i+1
        #if i==1:
            #buferr_book=[]
            #name_book,id__livelib2 =find_all_name(soup)
            #buferr_book.append(name_book)

            #athor_recendent,athor_recendent_nummbers= find_all_name_all_big(soup)
            #book__namerr=str(buferr_book[0])



            #for athor,nummb in  zip(athor_recendent,athor_recendent_nummbers):
                #funncct_get_db(book__namerr , id__livelib2 ,  athor ,  nummb)



        #else:
            #athor_recendent,athor_recendent_nummber =find_all_name_all_big(soup)
            #for athor,nummb in  zip(athor_recendent,athor_recendent_nummbers):
                #funncct_get_db(book__namerr , id__livelib2 ,  athor ,  nummb)



        #next=find_flag_next(soup)

        #if  next==''  or  i==6:

            #db_session.commit()
            #break
        #time.sleep(random.randint(7, 30))
        #bufer_nachalo_poisk=cconst_nacchalo_zagotov+str(next)
        #shtml=get_html(bufer_nachalo_poisk)
