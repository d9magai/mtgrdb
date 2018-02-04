from requests import get
import aiohttp
import asyncio
import os
import psycopg2
import random
import requests
import string
import textwrap
import tqdm

string = textwrap.dedent('''
SELECT
name,
id,
setcode,
type,
'https://magiccards.info/scans/en/' ||
CASE setcode
  WHEN 'p15A' THEN '15ann'
  WHEN 'ALL' THEN 'ai'
  WHEN 'MPS_AKH' THEN 'mpsakh'
  WHEN 'ATH' THEN 'at'
  WHEN 'ATQ' THEN 'aq'
  WHEN 'APC' THEN 'ap'
  WHEN 'ARN' THEN 'an'
  WHEN 'pARL' THEN 'arena'
  WHEN 'pALP' THEN 'apac'
  WHEN 'BRB' THEN 'br'
  WHEN 'BTD' THEN 'bd'
  WHEN 'pCEL' THEN 'uqc'
  WHEN 'pCMP' THEN 'cp'
  WHEN 'CHR' THEN 'ch'
  WHEN 'CP1' THEN 'clash'
  WHEN 'CP2' THEN 'clash'
  WHEN 'CP3' THEN 'mbp'
  WHEN '6ED' THEN '6e'
  WHEN 'CSP' THEN 'cs'
  WHEN 'CST' THEN 'cstd'
  WHEN 'CM1' THEN 'cma'
  WHEN 'CON' THEN 'cfx'
  WHEN 'DST' THEN 'ds'
  WHEN 'DKM' THEN 'dm'
  WHEN 'DIS' THEN 'di'
  WHEN 'pDRC' THEN 'drc'
  WHEN 'DD3_DVD' THEN 'ddadvd'
  WHEN 'DD3_EVG' THEN 'ddaevg'
  WHEN 'DD3_GVL' THEN 'ddagvl'
  WHEN 'DD3_JVC' THEN 'ddajvc'
  WHEN 'DDC' THEN 'dvd'
  WHEN 'DDD' THEN 'gvl'
  WHEN 'DD2' THEN 'jvc'
  WHEN 'DDE' THEN 'pvc'
  WHEN '8ED' THEN '8e'
  WHEN 'undef' THEN '8eb'
  WHEN 'pELP' THEN 'euro'
  WHEN 'EXO' THEN 'ex'
  WHEN 'FEM' THEN 'fe'
  WHEN '5ED' THEN '5e'
  WHEN '4ED' THEN '4e'
  WHEN 'pFNM' THEN 'fnmp'
  WHEN 'DRB' THEN 'fvd'
  WHEN 'V09' THEN 'fve'
  WHEN 'V11' THEN 'fvl'
  WHEN 'V10' THEN 'fvr'
  WHEN 'pGPX' THEN 'gpx'
  WHEN 'GPT' THEN 'gp'
  WHEN 'pGRU' THEN 'guru'
  WHEN 'pGTW' THEN 'grc'
  WHEN 'pWPN' THEN 'grc'
  WHEN 'pHHO' THEN 'hho'
  WHEN 'HML' THEN 'hl'
  WHEN 'ICE' THEN 'ia'
  WHEN 'CEI' THEN 'cedi'
  WHEN 'INV' THEN 'in'
  WHEN 'pJGP' THEN 'jr'
  WHEN 'JUD' THEN 'ju'
  WHEN 'MPS' THEN 'mpskld'
  WHEN 'pLGM' THEN 'dcilm'
  WHEN 'pLPA' THEN 'mlp'
  WHEN 'LEG' THEN 'lg'
  WHEN 'LGN' THEN 'le'
  WHEN 'LEA' THEN 'al'
  WHEN 'LEB' THEN 'be'
  WHEN 'LRW' THEN 'lw'
  WHEN 'pMGD' THEN 'mgdc'
  WHEN 'pMPR' THEN 'mprp'
  WHEN 'pMEI' THEN 'mbp'
  WHEN 'MMQ' THEN 'mm'
  WHEN 'MIR' THEN 'mr'
  WHEN 'MRD' THEN 'mi'
  WHEN 'MOR' THEN 'mt'
  WHEN 'MGB' THEN 'mgbc'
  WHEN 'NMS' THEN 'ne'
  WHEN '9ED' THEN '9e'
  WHEN 'undef' THEN '9eb'
  WHEN 'ODY' THEN 'od'
  WHEN 'ONS' THEN 'on'
  WHEN 'PLC' THEN 'pc'
  WHEN 'HOP' THEN 'pch'
  WHEN 'PLS' THEN 'ps'
  WHEN 'POR' THEN 'po'
  WHEN 'pPOD' THEN 'pot'
  WHEN 'PTK' THEN 'p3k'
  WHEN 'H09' THEN 'pds'
  WHEN 'pPRE' THEN 'ptc'
  WHEN 'pPRO' THEN 'pro'
  WHEN 'PCY' THEN 'pr'
  WHEN 'pREL' THEN 'rep'
  WHEN '3ED' THEN 'rv'
  WHEN 'RQS' THEN ''
  WHEN 'SCG' THEN 'sc'
  WHEN '7ED' THEN '7e'
  WHEN 'S99' THEN 'st'
  WHEN 'S00' THEN 'st2k'
  WHEN 'STH' THEN 'sh'
  WHEN 'pSUM' THEN 'sum'
  WHEN 'pSUS' THEN 'sus'
  WHEN 'TMP' THEN 'tp'
  WHEN 'DRK' THEN 'dk'
  WHEN 'TSP' THEN 'ts'
  WHEN 'TSB' THEN 'tsts'
  WHEN 'TOR' THEN 'tr'
  WHEN 'p2HG' THEN 'thgt'
  WHEN 'FRF_UGIN' THEN 'ugin'
  WHEN 'UGL' THEN 'ug'
  WHEN 'UNH' THEN 'uh'
  WHEN '2ED' THEN 'un'
  WHEN 'undef' THEN 'uhaa'
  WHEN 'UDS' THEN 'ud'
  WHEN 'ULG' THEN 'ul'
  WHEN 'USG' THEN 'us'
  WHEN 'VIS' THEN 'vi'
  WHEN 'VAN' THEN ''
  WHEN 'WTH' THEN 'wl'
  WHEN 'pWCQ' THEN 'wmcq'
  WHEN 'pWOR' THEN 'wrl'
  WHEN 'pWOS' THEN 'wotc'
  ELSE LOWER(setcode)
END
|| '/'
|| mcinumber || '.jpg' AS url
FROM cards
WHERE COALESCE(mcinumber, '')!='' AND 1=0 OR (type='Scheme' AND setcode='E01')
''')


def get_connection():
    return psycopg2.connect(
        'host=127.0.0.1 '
        'port=5432 '
        'dbname=postgres '
        'user=postgres '
        'password=secret '
    )


def get_dict_resultset():
    cur = get_connection().cursor()
    sql = string
    cur.execute(sql)
    columns = (
        'name',
        'id',
        'setcode',
        'type',
        'url',
    )
    results = []
    for row in cur.fetchall():
        results.append(dict(zip(columns, row)))
    return results
