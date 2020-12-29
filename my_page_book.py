import requests
import random
import time
import json

from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from get_html import get_HTML

  # поиск названия книги  
def parse_book_name(review):
    name_book = review.find("a" , class_="brow-book-name with-cycle").text
    return name_book

def parse_book_id(review):
    book_info = review.find("a" , class_="brow-book-name with-cycle")    
    list_for_slash = (book_info['href']).split('/')
    book_id = (list_for_slash[2]).split('-')
    return book_id[0]
 
    

# <a class="brow-book-name with-cycle" href="/book/1002436430-zavodnoj-apelsin-entoni-bjordzhess" title="Энтони Бёрджесс - Заводной апельсин">Заводной апельсин</a>

# поиск автора
def parse_book_author(review):
    author = review.find("a" , class_="brow-book-author")
    if author is None:
        return None
    return author.text
    
# оценка пользователя
def parse_book_score(review): 
    score = review.find("span" , class_="brow-rating marg-right").text
    return float(score)

def user_name(soup): #имя пользователя
    return soup.find('span' , class_ = 'header-profile-login').text
    

# создание массива из словарей    
def parse_books(html):
    all_about_book_list = []
    soup = BeautifulSoup(html , 'html.parser')
    for review in soup.find_all("div" , class_="brow-data"):    
        all_about_book_dir = {}
        all_about_book_dir['book_id'] = parse_book_id(review)
        all_about_book_dir['user'] = user_name(soup)
        all_about_book_dir['title'] = parse_book_name(review)
        all_about_book_dir['artist']  = parse_book_author(review)
        all_about_book_dir['score'] = parse_book_score(review)
        all_about_book_list.append(all_about_book_dir)
    return all_about_book_list





def new_page(url):
    result = get_HTML(url)
    soup = BeautifulSoup(result , 'html.parser')
    
    if soup.find('span' , id="a-list-page-next-") in soup.find_all('span', class_="pagination__page"):

        return result , 0
    return result , 1



if __name__ == "__main__":
    url = 'https://www.livelib.ru/reader/LushbaughPizzicato/read'    
    numb = 1
    page = 1
    all_page = []
    while page != 0:
        html, page = new_page(url + '~' + str(numb))

        all_page.extend(parse_books(html))
        random_numb = random.randint(7 , 30) 
        time.sleep(random_numb)
        numb += 1
        
        print(url + '~' + str(numb))
        print(all_page)
        




