
from bs4 import BeautifulSoup
from get_html import get_HTML
from my_page_book import parse_books
from add_data import store_books
# проверяем, есть ли информация нп странице

def information_in_html(url):
    html = get_HTML(url)
    if html:
        soup = BeautifulSoup(html , 'html.parser')
        return soup


# есть ли информация на этой странице

def stop_scrolling(soup):
    if soup:
        stop_word = soup.find("div" , class_="with-pad")  

        if stop_word is None or stop_word.text != 'Этот список пока пуст.':
            return True
        elif stop_word.text == 'Этот список пока пуст.':
            return False
        else:
            return True

# создание списка  рецензий пользователя из всех страниц

def all_page_rewiews(url , user_id):
    page_number = 1    

    keep_on = True
    while keep_on: 
        new_url = url + str(page_number) 
        print(new_url)
        soup  = information_in_html(new_url)
        keep_on = stop_scrolling(soup)
        if keep_on:
            one_page = parse_books(soup)
            add_or_not(one_page , user_id)

        page_number += 1 


# добовляем книги или пишим, что нет данных 
def add_or_not(one_page , user_id):
    if len(one_page) == 0:
        unknown = User.query.filter(User.id == user_id).first()
        unknown.how_much_read = None
        db_session.commit()
    else: 
        store_books(one_page)
    

if __name__ == "__main__":
    all_page_rewiews(url)