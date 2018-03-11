from collections import defaultdict
import textwrap


EXTRAS_CARDTYPE = [
    'Scheme',
    'Phenomenon',
    'Plane',
]

EXTRAS_PATH = defaultdict(lambda: 'plane/planechase-anthology', {
    'SchemeARC': 'scheme/archenemy',
    'SchemeE01': 'scheme/archenemy-nicol-bolas',
})

MAGICCARDS_ENDPOINT = 'https://magiccards.info'

GATHERER_WIZARDS_ENDPOINT = 'http://gatherer.wizards.com/Handlers/Image.ashx'

COLUMN = (
    'name',
    'id',
    'magiccardsinfocode',
    'setcode',
    'type',
    'types',
    'mcinumber',
    'multiverseid',
    'layout',
)


SQL_QUERY = textwrap.dedent('''
SELECT
c.name,
c.id,
s.magiccardsinfocode,
c.setcode,
c.type,
c.types,
c.mcinumber,
c.multiverseid,
c.layout
FROM cards c
JOIN sets AS s ON s.code=c.setcode
WHERE setcode NOT IN ('RQS', 'pPRE', 'A25')
''')
