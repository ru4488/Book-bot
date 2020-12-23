import requests
import random
import time
import json

from fake_useragent import UserAgent
from bs4 import BeautifulSoup


jar = requests.cookies.RequestsCookieJar()

def get_HTML(url):
    global jar
    try:
        result = requests.get(url , headers={'User-Agent': UserAgent().chrome}, cookies=jar)
        result.encoding = "utf8"
        jar = result.cookies
        return result.text
    except (requests.RequestException , ValueError):
        print('сетевая ошибка')
        return False


    
def parse_name_book(review):
    name_book = review.find("a" , class_="brow-book-name with-cycle").text
    return name_book



def parse_author_book(review):
    author = review.find("a" , class_="brow-book-author").text
    return author


def parse_score_book(review): 
    
    score = review.find("span" , class_="brow-rating marg-right").text
    return score
  

    
    
def parse_books(html):
    
    all_about_book_list = []
    soup = BeautifulSoup(html , 'html.parser')
    for review in soup.find_all("div" , class_="brow-data"):    
        all_about_book_dir = {}
        
        name_book = parse_name_book(review)
        author = parse_author_book(review)
        score = parse_score_book(review)
                
        all_about_book_dir['title'] = name_book
        all_about_book_dir['artist'] = author
        all_about_book_dir['score'] = score

        all_about_book_list.append(all_about_book_dir)
#  может быть несколько одинаковых прочитаных книг (с разными оценками)



   

    print(all_about_book_list)



        




if __name__ == "__main__":
    url = 'https://www.livelib.ru/reader/LushbaughPizzicato/read'
    

    html = get_HTML(url)
    parse_books(html)

