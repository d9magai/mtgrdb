import aiofiles
import aiohttp
import async_timeout
import asyncio
import os
import tqdm
from urldict import *


async def download_coroutine(session, dic):
    url = dic['url']
    with async_timeout.timeout(10):
        async with session.get(url, verify_ssl=False) as response:
            filename = os.path.basename(url)
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


async def main(loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        for dic in get_dict_resultset():
            await download_coroutine(session, dic)


if __name__ == '__main__':

    connector = aiohttp.TCPConnector()
    with aiohttp.ClientSession(connector=connector) as client:
        loop = asyncio.get_event_loop()
        coroutines = [download_coroutine(client, dic) for dic in get_dict_resultset()]
        loop.run_until_complete(wait_with_progress(coroutines))
