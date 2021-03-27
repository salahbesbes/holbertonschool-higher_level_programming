#!/usr/bin/python3
""" filter states modules """
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def filter_states():
    """ filter states by that contain "a" """

    user = sys.argv[1]
    password = sys.argv[2]
    dataBase = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, password, dataBase),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    load_state = session.query(State).filter(State.id == 2)

    try:
        load_state.name = "New Mexico"
        session.commit()
    except Exception:
        return


if __name__ == "__main__":
    filter_states()
