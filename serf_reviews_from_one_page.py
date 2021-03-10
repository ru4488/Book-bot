from all_books_on_one_page import all_reviews_on_one_page
from models import User , Review
from my_page_book import information_in_html
from add_data import store_books

    # сбор оценок пользователей и добавление их в таблицу при открывании 1000 оценках на странице  



# записан этот пользователь в базу данных или нет 
def add_or_not_to_database():
    users = User.query.filter(User.id > 1152).all()
    for row in users:
        how_much_add = Review.query.filter(Review.user_id == row.id).count()
        print(row.id)
        if row.how_much_read is None:
            print('удалили пользователя')
        elif row.how_much_read > how_much_add:
            url = 'https://www.livelib.ru/reader/' + row.name + '/read'
            user_name = row.name
            parsing_and_add_to_datebase(url , user_name)
            print(row.id , 'записан')
        print(row.id , 'уже был')
        
#  сбор и запись данных в базу данных

def parsing_and_add_to_datebase(url , user_name): 
        page_numb = 1
        html = ''
        print(url)
        while html != False:
            html = all_reviews_on_one_page(url , page_numb)
            one_page_info = get_dick_from_html(html , user_name) 
            html = add_to_datebase(one_page_info)
            page_numb += 1
            print("страница" , page_numb)
            if html == None:
                html == False
        
# получаем словарь из hml
def get_dick_from_html(html , user_name):
    if html != None:
        print('получаем словарь')
        one_page_info = information_in_html(html , user_name)
        return one_page_info
    return False

# добавляем в базу данных
def add_to_datebase(one_page_info):
    if (one_page_info != False) and (one_page_info != None):  
        print("зашли в store books")          
        store_books(one_page_info)
        return True
    return False


if __name__ == "__main__":
    add_or_not_to_database()