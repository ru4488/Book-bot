from all_books_on_one_page import all_reviews_on_one_page
from models import User , Review
from my_page_book import parse_books
from bs4 import BeautifulSoup
from add_data import store_books

    # сбор оценок пользователей и добавление их в таблицу при открывании 1000 оценках на странице  




def was_it_complite():
    users = User.query.all()
    for row in users:
        how_much_add = Review.query.filter(Review.user_id == row.id).count()
        if row.how_much_read > how_much_add:
            url = 'https://www.livelib.ru/reader/' + row.name + '/read'
            serf_reviews_on_one_page(url)
            print(row.id , 'записан')
        print(row.id , 'уже был')


def serf_reviews_on_one_page(url): 
        page_numb = 1
        html = ''
        print(url)
        while html != False:
            html = all_reviews_on_one_page(url , page_numb)
            one_page_info = user_review(html)
            page_numb += 1
            html = add_to_table(one_page_info)
            print(page_numb)
            if html == None:
                html == False
        

def user_review(html):
    if html != None:
        one_page_info = parse_books(html)
        return one_page_info

def add_to_table(one_page_info):
    if one_page_info != False:            
        store_books(one_page_info)
        return True
    return False


if __name__ == "__main__":
    was_it_complite()