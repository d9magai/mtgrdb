import aiofiles
import aiohttp
import async_timeout
import asyncio
import os
import tqdm
from urldict import *


sema = asyncio.BoundedSemaphore(5)


async def download_coroutine(session, dic):
    url = dic['url']
    dirname = '{}/downloads/{}'.format(
        os.getcwd(),
        dic['setcode'],
    )
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    filename = '{}/{}.jpg'.format(
        dirname,
        dic['id'],
    )

    with async_timeout.timeout(10):
        async with sema, session.get(url, verify_ssl=False) as response:
            async with aiofiles.open(filename, 'wb') as fd:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    await fd.write(chunk)
            return await response.release()


@asyncio.coroutine
def wait_with_progress(coros):
    for f in tqdm.tqdm(asyncio.as_completed(coros), total=len(coros)):
        yield from f


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    session = aiohttp.ClientSession(loop=loop)
    coroutines = [download_coroutine(session, dic) for dic in get_dict_resultset()]
    loop.run_until_complete(wait_with_progress(coroutines))
    session.close()
    loop.close()
