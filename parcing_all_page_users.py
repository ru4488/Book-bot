from sqlalchemy import Column, Integer, String, and_
from sqlalchemy.orm.exc import NoResultFound
from db import db_session
from models import User, Review
from get_html import get_HTML
from add_data import store_books
from bs4 import BeautifulSoup
from my_page_book import parse_books
import random
import time


def user_exist(row):
    url = 'https://www.livelib.ru/reader/' + row + '/read'
    print(url)
    result = get_HTML(url)    
    if result is not False:
        return result



def parcing_all_page_of_user():
    users = User.query.all()

    for row in users:
        books_recorded = Review.query.filter(Review.user_id == row.id).count()
        if row.how_much_read < books_recorded:
            
            result = user_exist(row.name)
            print(parse_books(result))


            random_numb = random.randint(7 , 15)
            time.sleep(random_numb)


            # soup = BeautifulSoup(result , 'html.parser')
            # web_adress = soup.find("a" , href="/reader/" + row.name + "/read")
            # if web_adress != None:
            #     user = User.query.filter(User.name == row.name).first()

            #     user.how_much_read = int(books[1])
                
            #     db_session.add(user)
            #     db_session.commit()

  

if __name__ == "__main__":
    parcing_all_page_of_user()