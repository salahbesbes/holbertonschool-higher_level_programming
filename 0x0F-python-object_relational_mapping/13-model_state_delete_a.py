#!/usr/bin/python3
""" delete instance modules """
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def delete_instance():
    """ delete instance after filter"""

    user = sys.argv[1]
    password = sys.argv[2]
    dataBase = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, password, dataBase),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session \
        .query(State) \
        .filter(State.name.like('%a%'))

    for state in states:
        session.delete(state)
    session.commit()


if __name__ == "__main__":
    delete_instance()
