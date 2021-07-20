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


# поиск автора
def parse_book_author(review):
    author = review.find("a" , class_="brow-book-author")
    if author is None:
        return None
    return author.text

# оценка пользователя
def parse_book_score(review):
    score = review.find("span" , class_="brow-rating marg-right").text
    return str(score)

def user_name(review): #имя пользователя
    # return soup.find('span' , class_ = 'header-profile-login').text
    a = review.find('div' , class_ = 'brow-ratings').text
    a = (a).split(":")
    a = a[0].split(' ')
    return a[1]

def parse_url(review):
    score = review.find("a" , class_="brow-book-name with-cycle").get('href')
    #print('parse_url_score=',(score))
    return str(score)



# создание массива из словарей
def parse_books(soup):
    all_about_book_list = []

    print("мы тут if")
    for review in soup.find_all("div" , class_="brow-data"):

        all_about_book_dir = {}
        all_about_book_dir['book_id'] = parse_book_id(review)
        all_about_book_dir['user'] = user_name(soup)
        all_about_book_dir['title'] = parse_book_name(review)
        all_about_book_dir['artist']  = parse_book_author(review)
        all_about_book_dir['score'] = parse_book_score(review)
        all_about_book_dir['Url'] = parse_url(review)

        all_about_book_list.append(all_about_book_dir)

    
    return all_about_book_list 


    
if __name__ == "__main__":
    # url = 'https://www.livelib.ru/reader/LushbaughPizzicato/read'
    url = "https://www.livelib.ru/reader/VartanPopov/read"
    
    parse_books(soup)
