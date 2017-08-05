#!/bin/bash
set -eu
cd $(dirname $0)

mkdir -p download
cd download

JSON_FILENAME=AllSets-x.json
if [ ! -e $JSON_FILENAME ]; then
    curl -sL https://mtgjson.com/json/${JSON_FILENAME}.zip | bsdtar -xf-
fi

for set in $(jq --raw-output 'keys[]' ${JSON_FILENAME}); do
mkdir -p $set;

PGPASSWORD=secret psql -h localhost -p 15432 -U postgres -t  -A -F $'\t' -c "SELECT
'sleep 1s && wget --retry-connrefused --tries=60 --waitretry=1 -O ' || setcode || '/' || id || '.jpg ' ||
'http://magiccards.info/scans/en/' || 
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
|| mcinumber || '.jpg'
FROM cards
WHERE 1=1
AND COALESCE(mcinumber, '')!=''
AND setcode='"$set"'
ORDER BY setcode;
" > $set.sh
chmod +x $set.sh

done

find ./ -name "*.sh" | split -l 10 

echo "
chmod +x ./xaa* && ./xaa* 1> ./outxaa* 2> ./errxaa* &
chmod +x ./xab* && ./xab* 1> ./outxab* 2> ./errxab* &
chmod +x ./xac* && ./xac* 1> ./outxac* 2> ./errxac* &
chmod +x ./xad* && ./xad* 1> ./outxad* 2> ./errxad* &
chmod +x ./xae* && ./xae* 1> ./outxae* 2> ./errxae* &
chmod +x ./xaf* && ./xaf* 1> ./outxaf* 2> ./errxaf* &
chmod +x ./xag* && ./xag* 1> ./outxag* 2> ./errxag* &
chmod +x ./xah* && ./xah* 1> ./outxah* 2> ./errxah* &
chmod +x ./xai* && ./xai* 1> ./outxai* 2> ./errxai* &
chmod +x ./xaj* && ./xaj* 1> ./outxaj* 2> ./errxaj* &
chmod +x ./xak* && ./xak* 1> ./outxak* 2> ./errxak* &
chmod +x ./xal* && ./xal* 1> ./outxal* 2> ./errxal* &
chmod +x ./xam* && ./xam* 1> ./outxam* 2> ./errxam* &
chmod +x ./xan* && ./xan* 1> ./outxan* 2> ./errxan* &
chmod +x ./xao* && ./xao* 1> ./outxao* 2> ./errxao* &
chmod +x ./xap* && ./xap* 1> ./outxap* 2> ./errxap* &
chmod +x ./xaq* && ./xaq* 1> ./outxaq* 2> ./errxaq* &
chmod +x ./xar* && ./xar* 1> ./outxar* 2> ./errxar* &
chmod +x ./xas* && ./xas* 1> ./outxas* 2> ./errxas* &
chmod +x ./xat* && ./xat* 1> ./outxat* 2> ./errxat* &
chmod +x ./xau* && ./xau* 1> ./outxau* 2> ./errxau* &
chmod +x ./xav* && ./xav* 1> ./outxav* 2> ./errxav* &
" > get.sh
chmod +x get.sh

