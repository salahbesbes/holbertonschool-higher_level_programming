#!/usr/bin/python3
""" filter states modules by name """
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def filter_states():
    """ filter states by name """

    user = sys.argv[1]
    password = sys.argv[2]
    dataBase = sys.argv[3]
    stateName = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, password, dataBase),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session \
        .query(State) \
        .filter(State.name == stateName) \
        .one_or_none()

    try:
        print(result.id)
    except Exception:
        print('Not found')


if __name__ == "__main__":
    filter_states()
