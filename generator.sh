#!/bin/bash
set -eu
cd $(dirname $0)

JSON_FILENAME=AllSets-x.json

if [ ! -e $JSON_FILENAME ]; then
    curl -sL https://mtgjson.com/json/${JSON_FILENAME}.zip | gunzip - > ${JSON_FILENAME}
fi

mkdir -p json
cp createtable.sql run.sql

for s in $(jq --raw-output 'keys[]' ${JSON_FILENAME}); do
    if [ ! -e json/$s.json ]; then
        jq '.["'$s'"].cards' ${JSON_FILENAME} > json/$s.json
    fi

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
SELECT * FROM json_to_recordset('["$(jq '.["'$s'"]' ${JSON_FILENAME} | jq -r 'del(.cards)' | sed -e "s/'/''/g;s/alternativeNames/alternativenames/;s/gathererCode/gatherercode/;s/magicCardsInfoCode/magiccardsinfocode/;s/magicRaritiesCodes/magicraritiescodes/;s/releaseDate/releasedate/;s/onlineOnly/onlineonly/;" -)"]') AS x(
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
    artist       ,
    border       ,
    cmc          ,
    colorIdentity,
    colors       ,
    flavor       ,
    foreignNames ,
    hand         ,
    imageName    ,
    layout       ,
    legalities   ,
    life         ,
    loyalty      ,
    manaCost     ,
    mciNumber    ,
    multiverseid ,
    name         ,
    names        ,
    number       ,
    originalText ,
    originalType ,
    power        ,
    printings    ,
    rarity       ,
    releaseDate  ,
    reserved     ,
    rulings      ,
    source       ,
    starter      ,
    subtypes     ,
    supertypes   ,
    text         ,
    timeshifted  ,
    toughness    ,
    type         ,
    types        ,
    variations   ,
    watermark    ,
    setcode
)

SELECT *, '$s' AS setcode FROM json_to_recordset('"$(cat json/$s.json | sed -e "s/'/''/g;s/manaCost/manacost/;s/colorIdentity/coloridentity/;s/imageName/imagename/;s/releaseDate/releasedate/;s/mciNumber/mcinumber/;s/foreignNames/foreignnames/;s/originalText/originaltext/;s/originalType/originaltype/;" -)"') AS x(

    id            text,
    artist        text,
    border        text,
    cmc           text,
    colorIdentity json,
    colors        json,
    flavor        text,
    foreignNames  json,
    hand          text,
    imageName     text,
    layout        text,
    legalities    json,
    life          text,
    loyalty       text,
    manaCost      text,
    mciNumber     text,
    multiverseid  text,
    name          text,
    names         json,
    number        text,
    originalText  text,
    originalType  text,
    power         text,
    printings     json,
    rarity        text,
    releaseDate   text,
    reserved      text,
    rulings       json,
    source        text,
    starter       text,
    subtypes      json,
    supertypes    json,
    text          text,
    timeshifted   text,
    toughness     text,
    type          text,
    types         json,
    variations    json,
    watermark     text
    );" >> run.sql
    echo $s
done

echo complete.

