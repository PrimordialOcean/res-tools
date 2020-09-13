#!/bin/sh
for file in `find . -type f`;
do
    echo $file
    iconv -f ASCII -t utf-8 $file > tmpfile
    mv tmpfile $file
done
exit