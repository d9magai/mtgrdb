import aiohttp
import asyncio
import random
import string
import tqdm

from urldict import *


def write_to_file(filename, content):
    f = open(filename, 'wb')
    f.write(content)
    f.close()


@asyncio.coroutine
def get(*args, **kwargs):
    response = yield from aiohttp.request('GET', *args, **kwargs)
    return (yield from response.read())


@asyncio.coroutine
def download_file(dic):
    url = dic['url']
    with (yield from r_semaphore):
        content = yield from asyncio.async(get(url))
        if not os.path.exists(dic['setcode']):
            os.mkdir(dic['setcode'])
        filename = '{}/downloads/{}/{}.jpg'.format(
            os.getcwd(),
            dic['setcode'],
            dic['id']
        )

        write_to_file(filename, content)


@asyncio.coroutine
def wait_with_progressbar(coros):
    for f in tqdm.tqdm(asyncio.as_completed(coros), total=len(coros)):
        yield from f


r_semaphore = asyncio.Semaphore(10)
coroutines = [download_file(dic) for dic in get_dict_resultset()]
eloop = asyncio.get_event_loop()
eloop.run_until_complete(wait_with_progressbar(coroutines))
eloop.close()
