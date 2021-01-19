#!/usr/bin/python3
""" no module """


def lookup(obj):
    """ search for all attributes in a class 
    args:
        obj (obj): ddd
    Return: list
    """
    return [el for el in dir(obj)]
