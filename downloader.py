from string import punctuation
import aiofiles
import async_timeout
import asyncio
import os
import psycopg2
import tqdm

from constant.downlaodjob import *
from constant.dsn import *


MTG_DOWNLOADS_PATH = 'mtgdownloads'
SEMAPHORE = asyncio.BoundedSemaphore(3)


class DownloadJob(object):

    def __init__(self, dic):
        self.__url = self.__get_url(dic)
        self.__dst = self.__get_dst(dic)

    def url(self):
        return self.__url

    def dst(self):
        return self.__dst

    def __get_extras_name_format(self, name):
        t = str.maketrans('', '', punctuation)
        return name.replace("-", " ").translate(t).lower().replace(" ", "-")

    def __get_url(self, dic):
        one_type = dic['types'][0] if isinstance(dic['types'], list) else None

        if one_type in EXTRAS_CARDTYPE:
            url = '{}/extras/{}/{}.jpg'.format(
                MAGICCARDS_ENDPOINT,
                EXTRAS_PATH[one_type + dic['setcode']],
                self.__get_extras_name_format(dic['name']),
            )
            return url

        if one_type == 'Vanguard' or not dic['mcinumber']:
            url = '{}?multiverseid={}&type=card'.format(
                GATHERER_WIZARDS_ENDPOINT,
                dic['multiverseid'],
            )
            return url

        return '{}/scans/en/{}/{}.jpg'.format(
            MAGICCARDS_ENDPOINT,
            MAGICCARDSINFO_TABLE.get(dic['setcode'], dic['setcode'].lower()),
            dic['mcinumber'],
        )

    def __get_dst(self, dic):
        return '{}/{}/{}.jpg'.format(
            MTG_DOWNLOADS_PATH,
            dic['setcode'],
            dic['id']
        )


class DbClient(object):

    def __init__(self):
        self.__cur = self.get_cursor()

    def get_cursor(self):
        return psycopg2.connect(
            'host={} port={} dbname={} user={} password={}'.format(
                HOST,
                PORT,
                DBNAME,
                USER,
                PASSWORD,
            )
        ).cursor()

    def get_sets(self):
        self.__cur.execute('SELECT code FROM sets')
        return [row[0] for row in self.__cur.fetchall()]

    def get_downloadjobs(self):
        self.__cur.execute(SQL_QUERY)
        columns = (
            'name',
            'id',
            'setcode',
            'type',
            'types',
            'mcinumber',
            'multiverseid',
            'layout',
        )
        downloadjobs = []
        for row in self.__cur.fetchall():
            dic = dict(zip(columns, row))
            downloadjobs.append(DownloadJob(dic))
        return downloadjobs


def init(dbclient):
    downloadsdir_path = '{}/{}/'.format(
        os.getcwd(),
        MTG_DOWNLOADS_PATH,
    )
    if not os.path.exists(downloadsdir_path):
        os.mkdir(downloadsdir_path)
    for set_name in dbclient.get_sets():
        setdir_path = '{}/{}/'.format(downloadsdir_path, set_name)
        if not os.path.exists(setdir_path):
            os.mkdir(setdir_path)


async def download_coroutine(session, downloadjob):
    with async_timeout.timeout(None):
        async with SEMAPHORE, session.get(downloadjob.url()) as response:
            async with aiofiles.open(downloadjob.dst(), 'wb') as fd:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    await fd.write(chunk)

            return await response.release()


@asyncio.coroutine
def wait_with_progress(coros):
    for f in tqdm.tqdm(asyncio.as_completed(coros), total=len(coros)):
        try:
            yield from f
        except Exception:
            pass


if __name__ == '__main__':
    dbclient = DbClient()
    init(dbclient)
