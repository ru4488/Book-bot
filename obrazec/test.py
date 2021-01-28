from multiprocessing.dummy import Pool as ThreadPool
import dbconnect
from urllib.request import *
import random
import re
import time
import lxml.html as html
from lxml import etree


cursor = dbconnect.connection()


def reqs(url):
    request = Request(url)
    ua_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2467.2 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko']
    request.add_header('User-Agent', random.choice(ua_list))
    return urlopen(request).read()

def get_info_html(res_html):
    tree = html.fromstring(res_html)
    el = tree.xpath("//div[@class='pages2']/text()")
    test = el[0]
    return int(re.search(r'\d+', test).group())

def main():
    cursor.execute("SELECT url FROM labirint")
    urls = cursor.fetchall()
    parse_urls = []
    t = time.clock()
    for url in urls:
       parse_urls.append(url[0])
    pool = ThreadPool(10)
    print('Метка 1 {:.3f} seconds'.format(time.clock() - t))
    result = pool.map(reqs, parse_urls)
    pool.close()
    pool.join()
    for res in result:
        print(get_info_html(res))
    print('Метка 1 {:.3f} seconds'.format(time.clock() - t))

if __name__ == '__main__':
    main()
