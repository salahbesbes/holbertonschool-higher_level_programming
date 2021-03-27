#!/usr/bin/python3
""" filter cities modules """
import sys
import MySQLdb


def filter_cities():
    """ filter cities by state """
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
    # cur.execute("SELECT name FROM cities WHERE state_id = \
    #             (SELECT id FROM states WHERE name = \'{}\' )"
    #             .format(stateName))

    cur.execute("SELECT cities.name \
                FROM cities \
                INNER JOIN states \
                ON cities.state_id = states.id \
                WHERE states.name LIKE BINARY %(stateName)s",
                {'stateName': stateName})
    cities = cur.fetchall()
    res = sep = ''
    for city in cities:
        res += sep + city[0]
        sep = ', '
    print(res)

    cur.close()
    db.close()


if __name__ == "__main__":
    filter_cities()
