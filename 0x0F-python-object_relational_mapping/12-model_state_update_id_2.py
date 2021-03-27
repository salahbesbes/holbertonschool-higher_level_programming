#!/usr/bin/python3
""" update instance modules """
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def update_instance():
    """ update instance where id = 2 """

    user = sys.argv[1]
    password = sys.argv[2]
    dataBase = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, password, dataBase),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    load_state = session \
        .query(State) \
        .filter(State.id == 2) \
        .one_or_none()
    try:
        load_state.name = "New Mexico"
        session.commit()
    except Exception:
        return


if __name__ == "__main__":
    update_instance()
