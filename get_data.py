from models import User, Review, Book
from sqlalchemy import and_
import  math  as  ma


def all_score_book(my_book):
    scores_list = []
    all_score_book = Review.query.filter(Review.book_id == my_book.id )
    for row in all_score_book:
        scores_list.append(row)
    return scores_list

def all_score_user(my_name):
    scores_list = []
    all_score_user = Review.query.filter(Review.user_id == my_name.id )
    for row in all_score_user:
        scores_list.append(row)
    return scores_list


def all_books_user(my_name , my_book):
    all_books_user_list = []
    books_user = Review.query.filter(Review.user_id == my_name.id , Review.book_id == my_book.id).first()
    all_books_user_list.append(books_user)
    return all_books_user_list

def  all__userr__book(my_book,my):
    my_scorre= Review.query.filter(Review.user_id == my.id , Review.book_id == my_book.id).first()
    #print(my_scorre.score)

    user_read=Review.query.filter( Review.book_id == my_book.id,Review.user_id != my.id  ).all()

    sppis=[]

    for uss  in  user_read:
        user_book_list={}
        user_book_list['modul_cene']=(abs(uss.score-my_scorre.score)  )
        user_book_list['user_id']=( uss.user_id )
        sppis.append(user_book_list)
    #for ret in sppis:
        #print('do sort ret=',ret)
    sppis.sort(key=lambda x: x['modul_cene'])
    #for ret in sppis:
        #print('posle  ret=',ret)
    return sppis
    #ma.max(sppis)
def  get_user(test_userr_all):
    #print(test_userr_all[0]['user_id'])
    User_bufer=User.query.filter(User.id==test_userr_all[0]['user_id']).first()
    #print(User_bufer.name)

    return  User_bufer
    #for iter  in  sppis:
        #print('iter=',iter)

book_score_dir = {}
my_book =  Book.query.first()
book_scores = all_score_book(my_book)
book_score_dir[my_book] = book_scores
# print(book_score_dir)


user_score_dir = {}
my_name = User.query.filter(User.name == "LushbaughPizzicato").first()
my_name = User.query.filter(User.name == "NikaTeymurova").first()

test_userr_all=all__userr__book(my_book,my_name)
User_name=get_user(test_userr_all)
print(User_name)

user_score = all_score_user(my_name)
user_score_dir[my_name] = user_score
# print(user_score_dir)

user_books_and_score_dir = {}
user_books_and_score = all_books_user(my_name , my_book)
user_books_and_score_dir[my_name] = user_books_and_score
