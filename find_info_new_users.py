from add_data import all_page_info , store_books
from models import User, Review, Book
import random
import time


if __name__ == "__main__":
    
    get_info_user = User.query.all()
    for row in get_info_user:
        url = 'https://www.livelib.ru/reader/' + row.name + '/read'

        all_info = all_page_info(url)
        store_books(all_info)
        random_numb = random.randint(7 , 30)
        time.sleep(random_numb)

        print(url)