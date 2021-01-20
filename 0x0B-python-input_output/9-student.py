#!/usr/bin/python3
""" module """
import json


class Student:
    """description for student class """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieve info to json format """
        return vars(self)
