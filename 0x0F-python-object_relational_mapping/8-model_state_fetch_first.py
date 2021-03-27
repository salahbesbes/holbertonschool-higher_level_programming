#!/usr/bin/python3
""" list first state modules """
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def list_all_states():
    """ list first state of the table states """

    user = sys.argv[1]
    password = sys.argv[2]
    dataBase = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, password, dataBase),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        first_state = session.query(State).order_by(State.id).first()
        print('{}: {}'.format(first_state.id, first_state.name))
    except Exception:
        print('Nothing')


if __name__ == "__main__":
    list_all_states()
