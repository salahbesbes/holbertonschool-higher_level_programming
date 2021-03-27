#!/usr/bin/python3
""" list list_all_cities """
import sys
from model_city import Base, City
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import aliased


def list_all_cities():
    """ list list_all_cities """

    user = sys.argv[1]
    password = sys.argv[2]
    dataBase = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, password, dataBase),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City, State) \
        .filter(City.state_id == State.id)

    for city, state in result:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))


if __name__ == "__main__":
    list_all_cities()
