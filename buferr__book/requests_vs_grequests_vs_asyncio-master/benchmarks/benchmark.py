import asyncio
import time

import grequests
import requests
from requests_threads import AsyncSession

from benchmarks.private_settings import APP_ID, APP_SECRET


ACCESS_TOKEN = APP_ID + "|" + APP_SECRET

urls = [
    'https://graph.facebook.com/v2.10/67920382572/feed/?limit=100'
    '&access_token={}&since=2017-07-10&until=2017-07-23&fields=reactions.'
    'type(LIKE).limit(0).summary(total_count)'.format(ACCESS_TOKEN),
    'https://graph.facebook.com/v2.10/67920382572/feed/?limit=100&'
    'access_token={}&since=2017-07-10&until=2017-07-23&fields=reactions.'
    'type(LOVE).limit(0).summary(total_count)'.format(ACCESS_TOKEN),
    'https://graph.facebook.com/v2.10/67920382572/feed/?limit=100&'
    'access_token={}&since=2017-07-10&until=2017-07-23&fields=reactions.'
    'type(WOW).limit(0).summary(total_count)'.format(ACCESS_TOKEN),
    'https://graph.facebook.com/v2.10/67920382572/feed/?limit=100&'
    'access_token={}&since=2017-07-10&until=2017-07-23&fields=reactions.'
    'type(HAHA).limit(0).summary(total_count)'.format(ACCESS_TOKEN),
    'https://graph.facebook.com/v2.10/67920382572/feed/?limit=100&'
    'access_token={}&since=2017-07-10&until=2017-07-23&fields=reactions.'
    'type(SAD).limit(0).summary(total_count)'.format(ACCESS_TOKEN),
    'https://graph.facebook.com/v2.10/67920382572/feed/?limit=100'
    '&access_token={}&since=2017-07-10&until=2017-07-23&fields=reactions.'
    'type(ANGRY).limit(0).summary(total_count)'.format(ACCESS_TOKEN)
]
number_or_repetitions = 10


def requests_benchmark():
    start = time.time()

    for _ in range(number_or_repetitions):
        for url in urls:
            requests.get(url)

    print('Average elapsed time requests = {}'.format(
        (time.time() - start)/number_or_repetitions))


def grequests_benchmark():
    start = time.time()

    for _ in range(number_or_repetitions):
        requests_ = (grequests.get(u) for u in urls)
        grequests.map(requests_)

    print('Average elapsed time grequests = {}'.format(
        (time.time() - start) / number_or_repetitions))


async def asyncio_benchmark():
    start = time.time()

    for _ in range(number_or_repetitions):
        futures = [loop.run_in_executor(None, requests.get, url)
                   for url in urls]

        for future in futures:
            await future
    print('Average elapsed time asyncio = {}'.format(
        (time.time() - start) / number_or_repetitions))


async def requests_threads_benchmark():
    start = time.time()
    for _ in range(number_or_repetitions):
        for url in urls:
            await session.get(url)

    print('Average elapsed time requests_threads = {}'.format(
        (time.time() - start) / number_or_repetitions))


if __name__ == '__main__':
    requests_benchmark()
    grequests_benchmark()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio_benchmark())

    session = AsyncSession(n=100)
    session.run(requests_threads_benchmark)
