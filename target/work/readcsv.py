#!/usr/bin/python


import csv
table="target"

c = csv.reader(open("target.csv", "rb"))
sqlfile = open("target.sql", "w+")
count=0
for line in c:
    #if len(line) != 2:
    #print line[1]
    #sqlfile.write("insert %s(url, count) values(\"%s\",'%s')" % (table, line[0], line[1]))
    count += 1
    if count == 1:
	sqlfile.write("insert %s(url, count) values(\"%s\",'%s')" % (table, line[0], line[1]))

    elif count >= 1000:
	sqlfile.write(",\n (\"%s\",'%s');\n" % (line[0], line[1]))
	count = 0
    else:
    	sqlfile.write(",\n (\"%s\",'%s')" % (line[0], line[1]))


sqlfile.close()

