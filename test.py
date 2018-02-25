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
