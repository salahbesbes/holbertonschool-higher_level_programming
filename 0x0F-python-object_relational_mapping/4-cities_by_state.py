#!/usr/bin/python3
""" print cities """
import sys
import MySQLdb


def print_all_cities():
    """ print all cities """
    user = sys.argv[1]
    password = sys.argv[2]
    dataBase = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=user,
                         passwd=password,
                         db=dataBase)

    cur = db.cursor()

    # cur.execute("SELECT id, name, (SELECT name \
    #                     FROM states \
    #                     WHERE id = state_id) FROM cities\
    #              ORDER BY id ASC")
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities\
                INNER JOIN states\
                ON cities.state_id = states.id\
                ORDER BY id ASC")
    cities = cur.fetchall()
    for city in cities:
        print(city)

    cur.close()
    db.close()


if __name__ == "__main__":
    print_all_cities()
