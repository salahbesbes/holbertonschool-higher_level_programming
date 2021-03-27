#!/usr/bin/python3
import MySQLdb
import sys

user = sys.argv[1]
password = sys.argv[2]
dataBase = sys.argv[3]

db = MySQLdb.connect(host='localhost', user=user,
                     passwd=password, db=dataBase)

cur = db.cursor()

cur.execute("SELECT * FROM states ORDER BY id ASC")
states = cur.fetchall()
for state in states:
    print(state)
