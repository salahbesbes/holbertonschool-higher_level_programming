#!/usr/bin/python3
""" list all states modules """
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def list_all_states():
    """ list all states of the table states """

    user = sys.argv[1]
    password = sys.argv[2]
    dataBase = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, password, dataBase),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State)
    for state in states:
        print('{}: {}'.format(state.id, state.name))


if __name__ == "__main__":
    list_all_states()
