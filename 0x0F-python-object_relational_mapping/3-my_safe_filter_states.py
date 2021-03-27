#!/usr/bin/python3
import MySQLdb
import sys

user = sys.argv[1]
password = sys.argv[2]
dataBase = sys.argv[3]
stateName = sys.argv[4]
db = MySQLdb.connect(host='localhost', user=user, passwd=password,
                     db=dataBase)

cur = db.cursor()
cur.execute("""SELECT * FROM states WHERE name = {} """.format(stateName))
names = cur.fetchall()
for name in names:
    print(name)
