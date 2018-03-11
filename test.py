import unittest
from downloader import DownloadJob


class TestDownloadJob(unittest.TestCase):
    """test class of tashizan.py
    """

    def test_scheme(self):
        dic = {
            'name': 'Realms Befitting My Majesty',
            'id': 'f1b860777f4f774d7a3adcf41291006f84df7424',
            'magiccardsinfocode': 'arc',
            'setcode': 'ARC',
            'type': 'Scheme',
            'types': ['Scheme'],
            'mcinumber': None,
            'multiverseid': '212653',
            'layout': 'scheme',
        }
        self.assertEqual('https://magiccards.info/extras/scheme/archenemy/realms-befitting-my-majesty.jpg', DownloadJob(dic).url())

    def test_plane(self):
        dic = {
            'name': 'Bloodhill Bastion',
            'id': 'ecd7436040a3d511ba4825a4b2ecf0ce3f2deccf',
            'magiccardsinfocode': 'pca',
            'setcode': 'PCA',
            'type': 'Plane — Equilor',
            'types': ['Plane'],
            'mcinumber': None,
            'multiverseid': '423597',
            'layout': 'plane',
        }
        self.assertEqual('https://magiccards.info/extras/plane/planechase-anthology/bloodhill-bastion.jpg', DownloadJob(dic).url())

    def test_phenomenon(self):
        dic = {
            'name': 'Planewide Disaster',
            'id': '921befc6dd3a37e65eaba484721f573c8172d16f',
            'magiccardsinfocode': 'pc2',
            'setcode': 'PC2',
            'type': 'Phenomenon',
            'types': ['Phenomenon'],
            'mcinumber': None,
            'multiverseid': '226545',
            'layout': 'phenomenon',
        }
        self.assertEqual('https://magiccards.info/extras/plane/planechase-anthology/planewide-disaster.jpg', DownloadJob(dic).url())

    def test_vanguard(self):
        dic = {
            'name': 'Serra Angel Avatar',
            'id': '59f7d4bdeb18b5962817ae60d94878ee558bcc50',
            'magiccardsinfocode': '',
            'setcode': 'VAN',
            'type': 'Vanguard',
            'types': ['Vanguard'],
            'mcinumber': None,
            'multiverseid': '205492',
            'layout': 'vanguard',
        }
        self.assertEqual('http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=205492&type=card', DownloadJob(dic).url())

    def test_token(self):
        dic = {
            'name': 'Elemental Shaman',
            'id': '39bde9d9c9d90d2008870efbafb9ee53a3a6a408',
            'magiccardsinfocode': 'jvc',
            'setcode': 'DD2',
            'type': 'Creature — Elemental Shaman',
            'types': ['Creature'],
            'mcinumber': None,
            'multiverseid': '190199',
            'layout': 'token',
        }
        self.assertEqual('http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=190199&type=card', DownloadJob(dic).url())

    def test_s00(self):
        dic = {
            'name': 'Orcish Oriflamme',
            'id': '83fa833e814302fab6ac41e2db0e76c276d14b2a',
            'magiccardsinfocode': 'st2k',
            'setcode': 'S00',
            'type': 'Enchantment',
            'types': ['Enchantment'],
            'mcinumber': None,
            'multiverseid': '25540',
            'layout': 'normal',
        }
        self.assertEqual('http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=25540&type=card', DownloadJob(dic).url())

    def test_not_mcinumber(self):
        dic = {
            'name': "Urza's Mine",
            'id': '7c921a805e6b8b0dd67233b3cfee38d48c6eaeb6',
            'magiccardsinfocode': 'me4',
            'setcode': 'ME4',
            'type': 'Land — Urza’s Mine',
            'types': ['Land'],
            'mcinumber': None,
            'multiverseid': '220947',
            'layout': 'normal',
        }
        self.assertEqual('http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=220947&type=card', DownloadJob(dic).url())

    def test_basic(self):
        dic = {
            'name': "Ancestor's Chosen",
            'id': 'ab1ab474019e4e76c66e2b524d354cb7c3212616',
            'magiccardsinfocode': '10e',
            'setcode': '10E',
            'type': 'Creature — Human Cleric',
            'types': ['Creature'],
            'mcinumber': '1',
            'multiverseid': '130550',
            'layout': 'normal',
        }
        self.assertEqual('https://magiccards.info/scans/en/10e/1.jpg', DownloadJob(dic).url())

    def test_ugl_token(self):
        dic = {
            'name': 'Squirrel token card',
            'id': 'a47493808a9b33587743267eb4934b8de4ce09fc',
            'magiccardsinfocode': 'ug',
            'setcode': 'UGL',
            'type': '',
            'types': None,
            'mcinumber': None,
            'multiverseid': '5607',
            'layout': 'token',
            'url': None
        }
        self.assertEqual('http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=5607&type=card', DownloadJob(dic).url())

    def test_dst(self):
        dic = {
            'name': 'Squirrel token card',
            'id': 'a47493808a9b33587743267eb4934b8de4ce09fc',
            'magiccardsinfocode': 'ug',
            'setcode': 'UGL',
            'type': '',
            'types': None,
            'mcinumber': None,
            'multiverseid': '5607',
            'layout': 'token',
            'url': None
        }
        self.assertEqual('mtgdownloads/UGL/a47493808a9b33587743267eb4934b8de4ce09fc.jpg', DownloadJob(dic).dst())


if __name__ == "__main__":
    unittest.main()
