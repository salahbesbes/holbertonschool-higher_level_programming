#!/usr/bin/python3
""" module """


class Student:
    """description for student class """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieve info to json format """
        new = {}
        if attrs is None:
            return vars(self)
        else:
            for el in attrs:
                if el in vars(self):
                    new[el] = vars(self)[el]
        return new

    def reload_from_json(self, json):
        vars(self).update(json)
