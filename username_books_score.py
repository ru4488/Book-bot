import requests
import random
import redis
import time
import json
from get_html import get_HTML

from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from ratelimit  import *

def last_page(pages):
        soup = BeautifulSoup(pages, 'html.parser')
        info= soup.find("a" , title= "Последняя страница") 
        last_page_list = info['href'].split('~')  
        last_page = int(last_page_list[1])
        return last_page



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
    all_about_book_list = []
    for review in soup.find_all('div', class_="block-border card-block expert-review"):
        info= review.find("div" , class_="group-login-date dont-author")   
        info_list = info.text.split()
        all_about_book_list.extend(teg_book(info_list, review))
    return all_about_book_list




if __name__ == "__main__":
    
    url = 'https://www.livelib.ru/reader/Fari22/reviews'
    pages = get_HTML('https://www.livelib.ru/reader/Fari22/reviews~1')
    
    last_page = last_page(pages)  
    all_page_list = []
    for web_page in range(1 , last_page + 1):
        all_page_list.append(url + '~' + str(web_page))
    print(last_page)
 
    new_page = []
    for i in range(len(all_page_list)):
        random_numb = random.randint(7 , 30) 
        html = get_HTML(all_page_list[i])    
        new_page.extend(all_about_books(html))
        time.sleep(random_numb)
    print(new_page)
    with open("reviews_of_all_users_books.json", "w") as write_file:
        json.dump(new_page, write_file)