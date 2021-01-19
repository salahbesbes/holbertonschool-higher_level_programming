#!/usr/bin/python3
""" no module """


def add_attribute(obj, att, val):
    """docstring for add_attribute"""

    if hasattr(obj, '__dict__'):
        obj.__setattr__(att, val)
    else:
        raise TypeError("can't add new attribute")
