from models import User, Review, Book


"Список оценок книги под Book.id 759 "
users_with_same_score = []
user_with_same_score = {}
all_score = []
all_users = []
result = Review.query.filter(Review.book_id.in_([759]))
for row in result:
    # print(row.score)
    if row.score not in all_score:
        all_score.append(row.score)
        user_with_same_score[row.score] = "" 


''' список авторов через оценки '''
for row in result:   
    if row.score in all_score:
        all_users.append(row.user.name)        
print(all_users)

"словарь пользователи поставившие одинаковую оценку"
for row in result: 
    user_with_same_score = {}
    user_with_same_score[row.score] = row.user.name
    users_with_same_score.append(user_with_same_score)

print(users_with_same_score)








