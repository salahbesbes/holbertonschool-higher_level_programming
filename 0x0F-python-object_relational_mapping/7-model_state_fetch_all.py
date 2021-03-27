#!/usr/bin/python3
"""task 7
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

import sys

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
