import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import json

jar = requests.cookies.RequestsCookieJar()

# делаем больше 20 запросов на страницу пользователя

def all_reviews_on_one_page(url , page_numb):
    global jar
    headers = {
        'User-Agent': UserAgent().chrome,
        'X-Requested-With': 'XMLHttpRequest'
    }
    data = {
        'page_no': page_numb,
        'per_page': 1000,
        'is_new_design': "ll2019",
        'is_prev': "false"
    }
    result = requests.post(url, data=data, headers=headers ,  cookies=jar)
    result.raise_for_status()
    result.encoding = "utf8"
    jar = result.cookies
    result_jason = json.loads(result.text)
    if 'content' in result_jason:
        html =  result_jason['content']
        return html

    
if __name__ == "__main__":
    url = 'https://www.livelib.ru/reader/nad1204/read'
    page_numb = 1
    print(all_reviews_on_one_page(url , page_numb))







