import unittest
from urldict import *


class TestTashizan(unittest.TestCase):
    """test class of tashizan.py
    """

    def test_scheme(self):
        dic = {
            'name': 'Realms Befitting My Majesty',
            'id': 'f1b860777f4f774d7a3adcf41291006f84df7424',
            'setcode': 'ARC',
            'type': 'Scheme',
            'types': ['Scheme'],
            'mcinumber': None,
            'multiverseid': '212653',
            'layout': 'scheme',
            'url': None,
        }
        self.assertEqual('https://magiccards.info/extras/scheme/archenemy/realms-befitting-my-majesty.jpg', get_url(dic))

    def test_plane(self):
        dic = {
            'name': 'Bloodhill Bastion',
            'id': 'ecd7436040a3d511ba4825a4b2ecf0ce3f2deccf',
            'setcode': 'PCA',
            'type': 'Plane — Equilor',
            'types': ['Plane'],
            'mcinumber': None,
            'multiverseid': '423597',
            'layout': 'plane',
            'url': None,
        }
        self.assertEqual('https://magiccards.info/extras/plane/planechase-anthology/bloodhill-bastion.jpg', get_url(dic))

    def test_phenomenon(self):
        dic = {
            'name': 'Planewide Disaster',
            'id': '921befc6dd3a37e65eaba484721f573c8172d16f',
            'setcode': 'PC2',
            'type': 'Phenomenon',
            'types': ['Phenomenon'],
            'mcinumber': None,
            'multiverseid': '226545',
            'layout': 'phenomenon',
            'url': None,
        }
        self.assertEqual('https://magiccards.info/extras/plane/planechase-anthology/planewide-disaster.jpg', get_url(dic))

    def test_vanguard(self):
        dic = {
            'name': 'Serra Angel Avatar',
            'id': '59f7d4bdeb18b5962817ae60d94878ee558bcc50',
            'setcode': 'VAN',
            'type': 'Vanguard',
            'types': ['Vanguard'],
            'mcinumber': None,
            'multiverseid': '205492',
            'layout': 'vanguard',
            'url': None,
        }
        self.assertEqual('http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=205492&type=card', get_url(dic))

    def test_token(self):
        dic = {
            'name': 'Elemental Shaman',
            'id': '39bde9d9c9d90d2008870efbafb9ee53a3a6a408',
            'setcode': 'DD2',
            'type': 'Creature — Elemental Shaman',
            'types': ['Creature'],
            'mcinumber': None,
            'multiverseid': '190199',
            'layout': 'token',
            'url': None
        }
        self.assertEqual('http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=190199&type=card', get_url(dic))

    def test_s00(self):
        dic = {
            'name': 'Orcish Oriflamme',
            'id': '83fa833e814302fab6ac41e2db0e76c276d14b2a',
            'setcode': 'S00',
            'type': 'Enchantment',
            'types': ['Enchantment'],
            'mcinumber': None,
            'multiverseid': '25540',
            'layout': 'normal',
            'url': None
        }
        self.assertEqual('http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=25540&type=card', get_url(dic))

    def test_not_mcinumber(self):
        dic = {
            'name': "Urza's Mine",
            'id': '7c921a805e6b8b0dd67233b3cfee38d48c6eaeb6',
            'setcode': 'ME4',
            'type': 'Land — Urza’s Mine',
            'types': ['Land'],
            'mcinumber': None,
            'multiverseid': '220947',
            'layout': 'normal',
            'url': None
        }
        self.assertEqual('http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=220947&type=card', get_url(dic))

    def test_basic(self):
        dic = {
            'name': "Ancestor's Chosen",
            'id': 'ab1ab474019e4e76c66e2b524d354cb7c3212616',
            'setcode': '10E',
            'type': 'Creature — Human Cleric',
            'types': ['Creature'],
            'mcinumber': '1',
            'multiverseid': '130550',
            'layout': 'normal',
            'url': 'https://magiccards.info/scans/en/10e/1.jpg'
        }
        self.assertEqual('https://magiccards.info/scans/en/10e/1.jpg', get_url(dic))


if __name__ == "__main__":
    unittest.main()
