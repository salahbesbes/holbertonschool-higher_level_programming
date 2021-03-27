#!/usr/bin/python3
""" select state module """
import MySQLdb
import sys


def print_all_states():
    user = sys.argv[1]
    password = sys.argv[2]
    dataBase = sys.argv[3]

    """ print all table """
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=user,
                         passwd=password,
                         db=dataBase)

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()


if __name__ == "__main__":
    print_all_states()
