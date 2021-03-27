#!/usr/bin/python3
""" print state modul """
import MySQLdb
import sys


def print_state():
    """ print state  """
    user = sys.argv[1]
    password = sys.argv[2]
    dataBase = sys.argv[3]
    stateName = sys.argv[4]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=user,

                         passwd=password,
                         db=dataBase)

    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name = \'{}\''.format(stateName))
    names = cur.fetchall()
    for name in names:
        print(name)

    cur.close()
    db.close()


if __name__ == "__main__":
    print_state()
