#!/usr/bin/python


import csv
table="tigerdirect"

f = open("tigerdirect.txt", "rb")
sqlfile = open("tigerdirect.sql", "w+")
count=0
for line in f.readlines():
    #if len(line) != 2:
    #print line[1]
    #sqlfile.write("insert %s(url, count) values(\"%s\",'%s')" % (table, line[0], line[1]))
    pos = line.rfind(" ")
    if pos<=0:
        continue
    url = line[:pos].strip()
    cnt = line[pos+1:].strip()
    count += 1
    if count == 1:
	   sqlfile.write("insert %s(url, count) values(\"%s\",'%s')" % (table, url, cnt))
    elif count >= 1000:
	   sqlfile.write(",\n (\"%s\",'%s');\n" % (url, cnt))
	   count = 0
    else:
    	sqlfile.write(",\n (\"%s\",'%s')" % (url, cnt))


sqlfile.close()

