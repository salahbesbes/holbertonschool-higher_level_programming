#!/usr/bin/python3
import MySQLdb
import sys

user = sys.argv[1]
password = sys.argv[2]
dataBase = sys.argv[3]
stateName = sys.argv[4]

db = MySQLdb.connect(host='localhost', user=user,
                     passwd=password, db=dataBase)

cur = db.cursor()
cur.execute("SELECT name FROM cities WHERE state_id = \
            (SELECT id FROM states WHERE name = \'{}\' )"
            .format(stateName))
cities = cur.fetchall()
res = sep = ''
for city in cities:
    res += sep + city[0]
    sep = ', '
print(res)
