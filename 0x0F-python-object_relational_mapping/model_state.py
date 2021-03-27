#!/usr/bin/python3
""" create State Class mapped to table """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # metadata shared by all classes


class State(Base):
    """ State class represent single row in states table """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
