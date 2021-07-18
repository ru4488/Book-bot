import requests
from fake_useragent import UserAgent

jar = requests.cookies.RequestsCookieJar()

def get_HTML(url):
    global jar
    try:
        result = requests.get(url , headers={'User-Agent': UserAgent().chrome}, cookies=jar)
        result.raise_for_status()
        result.encoding = "utf8"
        jar = result.cookies
        return result.text


    except (requests.RequestException , ValueError):
        print('сетевая ошибка')
        return False
        
if __name__ == "__main__":
    get_HTML(url)

