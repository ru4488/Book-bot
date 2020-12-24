import requests
import random
import redis
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from ratelimit  import *
import time

jar = requests.cookies.RequestsCookieJar()


def get_HTML_first(url): #скачивает HTML файл 
    global jar
    try:    
        print(jar)
        result = requests.get(url , headers={'User-Agent': UserAgent().chrome} ,cookies=jar )
        result.raise_for_status()
        result.encoding = "utf8"
        jar = result.cookies
        
        # return result.text
        if not result.ok:
            print([])
        soup = BeautifulSoup(result.text, 'html.parser')
        info= soup.find("a" , title= "Последняя страница")   
        last_page_list = (''.join(str(info))).split()
        last_page_str = ''.join(last_page_list[3])
        last_page = int(last_page_str[-3 : -1])
        return last_page
    except (requests.RequestException , ValueError):
        print('сетевая ошибка')
        return False


# random_numb = random.randint(7 , 30) 
# @sleep_and_retry
# @limits(calls =1, period  = random_numb)
def get_HTML(html): #скачивает HTML файл 
    global jar
    try:    
        print(jar)
        result = requests.get(html , headers={'User-Agent': UserAgent().chrome}, cookies=jar)
        result.raise_for_status()
        result.encoding = "utf8"
        return result.text

    except (requests.RequestException , ValueError):
        print('сетевая ошибка')
        return False

def user_html(html): #cоздает HTML файд
    pass
    with open('user_score.html' , 'w' , encoding="utf8") as f:
        f.write(html) 


def teg_book(info_list, review):
    all_about_book_list = []
    all_about_book_dir = {}
    score_book = review.find('div' , class_="group-review-rating")
    score_list = score_book.text.split()  
   
    score = score_list[2]
    all_about_book_dir['score'] = score
#название книги
    if 'автора' in info_list:
        name_book_list = info_list[info_list.index('книгу') + 1 : info_list.index('автора')]
        name_book = " ".join(name_book_list)
            
        all_about_book_dir['title'] = name_book


            
            #нашел проблему на странице, есть места где нет слов "атовров/автора"
    elif 'авторов' in info_list: 
            
        name_book_list = info_list[info_list.index('книгу') + 1 : info_list.index('авторов')]
        name_book = " ".join(name_book_list)
            
        #     all_about_book_dir['title'] =  name_book


            
            

# имя автора книги
    if 'автора' in info_list:
        name_artist_list =info_list[info_list.index('автора') + 1 :]
        name_artist = " ".join(name_artist_list)
        all_about_book_dir['artist'] = name_artist
            

    elif 'авторов' in info_list:
        name_artist_list =info_list[info_list.index('авторов') + 1 :]
        name_artist = " ".join(name_artist_list)
        how_much_artists = name_artist.split(', ')
            
        for artist in range(len(how_much_artists)):
            all_about_book_dir1 = {}
            all_about_book_dir1['artist'] =  how_much_artists[artist]
            all_about_book_dir1['title'] = name_book
            all_about_book_dir1['score'] = score
            all_about_book_list.append(all_about_book_dir1)
                
                
    if len(all_about_book_dir) != 0: 
        all_about_book_list.append(all_about_book_dir)
        all_about_book_dir = {}
    
    return all_about_book_list

    
def all_about_books(html):

    soup = BeautifulSoup(html , 'html.parser')
    # about_books_data = soup.findAll("div" , class_="group-review-rating")
    
    # # name_user = soup.find('div' , class_ = "gp-rating").find('input')['value']
    # # print(name_user)
    all_about_book_list = []
    # all_about_book_dir = {}
    


    
    for review in soup.find_all('div', class_="block-border card-block expert-review"):
 
        info= review.find("div" , class_="group-login-date dont-author")   
        info_list = info.text.split()
        
#  # оценка книги --- в словарь 
        all_about_book_list.extend(teg_book(info_list, review))
#         score_book = review.find('div' , class_="group-review-rating")
#         score_list = score_book.text.split()  
   
#         score = score_list[2]
        
        
        
 
# #название книги
#         if 'автора' in info_list:
#             name_book_list = info_list[info_list.index('книгу') + 1 : info_list.index('автора')]
#             name_book = " ".join(name_book_list)
            
#             all_about_book_dir['title'] = name_book
#             all_about_book_dir['score'] = score

            
#             #нашел проблему на странице, есть места где нет слов "атовров/автора"
#         elif 'авторов' in info_list: 
            
#             name_book_list = info_list[info_list.index('книгу') + 1 : info_list.index('авторов')]
#             name_book = " ".join(name_book_list)
            
#         #     all_about_book_dir['title'] =  name_book


            
            

# # имя автора книги
#         if 'автора' in info_list:
#             name_artist_list =info_list[info_list.index('автора') + 1 :]
#             name_artist = " ".join(name_artist_list)
#             all_about_book_dir['artist'] = name_artist
            

#         elif 'авторов' in info_list:
#             name_artist_list =info_list[info_list.index('авторов') + 1 :]
#             name_artist = " ".join(name_artist_list)
#             how_much_artists = name_artist.split(', ')
            
#             for artist in range(len(how_much_artists)):
#                 all_about_book_dir1 = {}
#                 all_about_book_dir1['artist'] =  how_much_artists[artist]
#                 all_about_book_dir1['title'] = name_book
#                 all_about_book_dir1['score'] = score
#                 all_about_book_list.append(all_about_book_dir1)
                

        
    return all_about_book_list
    









if __name__ == "__main__":
    
    url = 'https://www.livelib.ru/reader/Fari22/reviews'
    last_page = get_HTML_first('https://www.livelib.ru/reader/Fari22/reviews~1')
       
    all_page_list = []
    for web_page in range(1 , last_page + 1):
        all_page_list.append(url + '~' + str(web_page))
 
 
    new_page = []
    for i in range(len(all_page_list)):
        random_numb = random.randint(7 , 30) 
        html = get_HTML(all_page_list[i])   
          
        new_page.extend(all_about_books(html))
        
        time.sleep(random_numb)
        print(new_page)