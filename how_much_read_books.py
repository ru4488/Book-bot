from sqlalchemy import Column, Integer, String, and_
from sqlalchemy.orm.exc import NoResultFound
from db import db_session
from models import User
from get_html import get_HTML
from add_data import store_books
from bs4 import BeautifulSoup
import random
import time

# Сколько прочел пользователь книг , дописал этот код, так как изначально не было этого столбца

def how_much_read_books():
    # users = User.query.filter(User.how_much_read == None).all()
    users = User.query.get(2)
    print(users)
    # for row in users:
        # url = 'https://www.livelib.ru/reader/' + row.name + '/read'
        # print(url)
        # result = get_HTML(url)
        # if result is not False:
        #     soup = BeautifulSoup(result , 'html.parser')
        #     web_adress = soup.find("a" , href="/reader/" + row.name + "/read")
        #     if web_adress != None:
        #         user = User.query.filter(User.name == row.name).first()
        #         books = web_adress.text.split(' ')    
        #         print(int(books[1]))
        #         user.how_much_read = int(books[1])
                
        #         db_session.add(user)
        #         db_session.commit()

        # random_numb = random.randint(7 , 15)
        # time.sleep(random_numb)  

if __name__ == "__main__":
    how_much_read_books()
