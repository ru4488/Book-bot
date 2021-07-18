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

# есть ли информация на странице пользователя
def information_in_html(url):
    html = get_HTML(url)
    if html:
        soup = BeautifulSoup(html , 'html.parser')
        return soup

def stop_scrolling(soup):
    stop_word = soup.find("div" , class_="with-pad")  
    
    if stop_word is None or stop_word.text != 'Этот список пока пуст.':
        return True
    elif stop_word.text == 'Этот список пока пуст.':
        return False
    else:
        return True

# создание списка со всеми оценками пользователя
def all_page_rewiews(url):
    counting = 1    
    all_page = []  
    keep_on = True
    while keep_on: 
        new_url = url + str(counting) 
        print(new_url)
        soup  = information_in_html(new_url)
        keep_on = stop_scrolling(soup)
        if keep_on:
            one_page = parse_books(soup)
            all_page.extend(one_page)
        counting += 1 
        rest = random.randint(3, 10)
        time.sleep(rest)
    print(len(all_page))
    return all_page
        

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
    
    information_in_html(url)
