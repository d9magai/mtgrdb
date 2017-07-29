#!/bin/bash
PGPASSWORD=secret psql -h localhost -p 15432 -U postgres -t  -A -F $'\t' -c "SELECT
'sleep 1s && wget --retry-connrefused --tries=60 --waitretry=1 -O ' || setcode || '/' || id || '.jpg ' ||
'http://magiccards.info/scans/en/' || 
CASE setcode 
  WHEN 'pWOS' THEN 'wotc' 
  ELSE LOWER(setcode)
END
|| '/'
|| mcinumber || '.jpg'
FROM cards
WHERE 1=1
AND COALESCE(mcinumber, '')!=''
AND setcode IN ('8EB', '9EB')
ORDER BY setcode;
" > shortrun.sh

