#!/usr/bin/python3


def lookup(obj):
    """ search for all attributes in a class """
    return [el for el in dir(obj)]
