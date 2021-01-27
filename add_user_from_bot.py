from add_data import all_page_info , store_books
from get_data import best_book_for_you
from models import User, Review, Book, Used_User



def new_user_from_bot(new_name):
    old_user = User.query.filter(User.name == new_name).first()
    if old_user == None:
        url = 'https://www.livelib.ru/reader/' + new_name + '/read'
        all_info = all_page_info(url)
        store_books(all_info)
       
    else:
        best_book_for_you(new_name)




# проверяет, есть ли такой пользователь в уже собраных книгах


new_name = "VartanPopov"
new_user_from_bot(new_name)

    # url = "https://www.livelib.ru/reader/VartanPopov/read"
    # "LushbaughPizzicato"
