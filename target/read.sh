#!/bin/sh

sqlfile="allrules.sql"
echo "" > $sqlfile
while read line
do
echo "insert target(url) value(\"$line\");\n" >> $sqlfile
done < allrules.csv

