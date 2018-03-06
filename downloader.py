from string import punctuation
from constant.downlaodjob import *


class DownloadJob(object):

    def __init__(self, dic):
        self.__url = self.__get_url(dic)

    def url(self):
        return self.__url

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
