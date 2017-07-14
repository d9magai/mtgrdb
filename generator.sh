#!/bin/bash
set -eu

curl -sL https://mtgjson.com/json/AllSets-x.json.zip | bsdtar -xf-

mkdir -p json
cp createtable.sql run.sql

for s in $(jq --raw-output 'keys[]' AllSets-x.json); do
    jq '.["'$s'"].cards' AllSets-x.json > json/$s.json

    echo "
INSERT INTO sets(
    name               ,
    alternativeNames   ,
    code               ,
    gathererCode       ,
    oldCode            ,
    magicCardsInfoCode ,
    magicRaritiesCodes ,
    releaseDate        ,
    border             ,
    type               ,
    block              ,
    onlineOnly         ,
    booster            ,
    translations       ,
    mkm_name           ,
    mkm_id
)
SELECT * FROM json_to_recordset('["$(jq '.["'$s'"]' AllSets-x.json  | jq -r 'del(.cards)' | sed -e "s/'/''/g;s/alternativeNames/alternativenames/;s/gathererCode/gatherercode/;s/magicCardsInfoCode/magiccardsinfocode/;s/magicRaritiesCodes/magicraritiescodes/;s/releaseDate/releasedate/;s/onlineOnly/onlineonly/;" -)"]') AS x(
    name               text,
    alternativeNames   text,
    code               text,
    gathererCode       text,
    oldCode            text,
    magicCardsInfoCode text,
    magicRaritiesCodes text,
    releaseDate        date,
    border             text,
    type               text,
    block              text,
    onlineOnly         text,
    booster            text,
    translations       text,
    mkm_name           text,
    mkm_id             text
    );

INSERT INTO cards(
 id           ,
 layout       ,
 name         ,
 names        ,
 manacost     ,
 cmc          ,
 colors       ,
 coloridentity,
 type         ,
 supertypes   ,
 types        ,
 subtypes     ,
 rarity       ,
 text         ,
 flavor       ,
 artist       ,
 number       ,
 power        ,
 toughness    ,
 loyalty      ,
 multiverseid ,
 variations   ,
 imagename    ,
 watermark    ,
 border       ,
 timeshifted  ,
 hand         ,
 life         ,
 reserved     ,
 releasedate  ,
 starter      ,
 mcinumber    ,
 rulings      ,
 foreignnames ,
 printings    ,
 originaltext ,
 originaltype ,
 legalities   ,
 source       ,
 setcode
)

SELECT *, '$s' AS setcode FROM json_to_recordset('"$(cat json/$s.json | sed -e "s/'/''/g;s/manaCost/manacost/;s/colorIdentity/coloridentity/;s/imageName/imagename/;s/releaseDate/releasedate/;s/mciNumber/mcinumber/;s/foreignNames/foreignnames/;s/originalText/originaltext/;s/originalType/originaltype/;" -)"') AS x(
    id text,
    layout text,
    name text,
    names text,
    manaCost text,
    cmc text,
    colors text,
    colorIdentity text,
    type text,
    supertypes text,
    types text,
    subtypes text,
    rarity text,
    text text,
    flavor text,
    artist text,
    number text,
    power text,
    toughness text,
    loyalty text,
    multiverseid text,
    variations text,
    imageName text,
    watermark text,
    border text,
    timeshifted text,
    hand text,
    life text,
    reserved text,
    releaseDate text,
    starter text,
    mciNumber text,
    rulings text,
    foreignNames text,
    printings text,
    originalText text,
    originalType text,
    legalities text,
    source text
    );" >> run.sql
    echo $s
done

echo complete.

