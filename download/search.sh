#!/bin/bash
set -eu
IFS='
'
for i in `cat list`
do

if [ ! -e $i ]; then
    basename $i .jpg
fi

done

