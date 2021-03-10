
import random
import time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


  # поиск названия книги +
def parse_book_name(review):
    book_name  = review.find("a" , class_="lists__book-title").text

    return book_name.strip()
    
# поиск id книги +
def parse_book_id(review):
    book_info = review.find("a" , class_ = "lists__book-title").get("href")
    list_for_slash = book_info.split('/')
    book_id = (list_for_slash[2]).split('-')
    return book_id[0]


# поиск автора +
def parse_book_author(review):
    all_author  = review.find_all("a" , class_="lists__author")

    if len(all_author) > 1 :
        all_autor_list = []
        for one_autor in all_author:
            if one_autor.get('title') not in all_autor_list:
                all_autor_list.append(one_autor.get('title'))
        return ', '.join(all_autor_list)

    elif len(all_author) == 1:
        return review.find("a" , class_="lists__author").get('title')


# оценка пользователя +
def parse_book_score(review):
    score  = review.find("div" , class_="lists__rating").text
    return str(score)

def user_name(review): #имя пользователя
    # return soup.find('span' , class_ = 'header-profile-login').text
    a = review.find('div' , class_ = 'brow-ratings').text
    a = (a).split(":")
    a = a[0].split(' ')
    return a[1]

# поиск URL  +
def parse_url(review):
    url  = review.find("a" , class_="lists__book-title").get('href')
    return str(url)

# есть ли информация на странице пользователя
def information_in_html(html , user_name):
    soup = BeautifulSoup(html , 'html.parser')
    print(soup)
    stop_word = soup.find("div" , class_="with-pad")
    if stop_word == None:
        print(1)
        return parse_books(soup , user_name)
    elif stop_word.text == 'Этот список пока пуст.':
        print(2)
        return False
    else:
        print(3)
        return parse_books(soup , user_name)


# создание массива из словарей
def parse_books(soup , user_name):
    all_about_book_list = []
    review = soup.find_all('div' , class_="lists__wrapper")

    # print(review)
    

    print("мы тут if")
    for review in soup.find_all("div" , class_="lists__wrapper"):

        all_about_book_dir = {}
        all_about_book_dir['book_id'] = parse_book_id(review)
        all_about_book_dir['user'] = user_name
        all_about_book_dir['title'] = parse_book_name(review)
        all_about_book_dir['artist']  = parse_book_author(review)
        all_about_book_dir['score'] = parse_book_score(review)
        all_about_book_dir['Url'] = parse_url(review)

        all_about_book_list.append(all_about_book_dir)

    # print(all_about_book_list) 


    
if __name__ == "__main__":
    # url = 'https://www.livelib.ru/reader/LushbaughPizzicato/read'
    # url = "https://www.livelib.ru/reader/VartanPopov/read"
    information_in_html(html)
