SELECT
    CASE 
        WHEN (c.layout='normal' OR c.layout='leveler' OR c.layout='double-faced') THEN 'convert -crop 276x203+18+45 ~/wd/mtgrdb/download/'
        WHEN (c.layout='flip') THEN
        CASE SUBSTR(mcinumber, LENGTH(mcinumber))
            WHEN 'a' THEN 'convert -crop 273x160+19+136 ~/wd/mtgrdb/download/'
            WHEN 'b' THEN 'convert -crop 273x160+19+143 ~/wd/mtgrdb/download/'
        END
    END
    || s.code || '/' || c.id || '.jpg ' || s.code || '/' || c.id || '.jpg'
FROM sets s JOIN cards c ON c.setcode=s.code
WHERE 
(('2003-05-26'<s.releasedate AND s.releasedate<='2014-06-06') OR (COALESCE(c.releasedate, '')!='' AND '2003-05-26'<c.releasedate AND c.releasedate<='2014-06-06'))
AND c.setcode NOT IN (
'pMEI',
'ME4'
)
AND c.id NOT IN (
'1d816e1e136f7c0b4dc4c117fc329c86d986668c',
'7c921a805e6b8b0dd67233b3cfee38d48c6eaeb6',
'3be4cd5932b52dffd581ab6613a6ad32393d31af',
'664a3e09ec3326f15ad5d59301ee794eaa065126',
'141dc186de847da17ad9a484775491762ba73627',
'f2f55e139baa31ff26f9f6b35b57cf9804ae6847',
'a481c341c9577959fd8f8795b2709a6e342417fc',
'4f8e418d3bdcce467ce943a4d17c508d8d61ce41',
'a009efcfd350cb1b28ab8e31fdcb732f4a8c1acc',
'da6d3fafa23719ac8571ef5b884f318e272a5f6a',
'0b91d1606d6c57fab7670ec843237d1920f621aa',
'849387ac6107e03799e353be7091fcc40c805123'
)
ORDER BY s.releasedate;

