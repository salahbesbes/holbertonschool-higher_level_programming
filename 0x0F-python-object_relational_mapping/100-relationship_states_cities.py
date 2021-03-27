#!/usr/bin/python3
""" filter states modules by name """
import sys
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def add_new_instances():
    """ filter states by name """

    user = sys.argv[1]
    password = sys.argv[2]
    dataBase = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, password, dataBase),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)  # create all Classes

    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)  # this hold the cities ref
    session.add_all([new_state, new_city])
    session.commit()
    session.close()


if __name__ == "__main__":
    add_new_instances()
