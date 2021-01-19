#!/usr/bin/python3
""" no module """


def inherits_from(obj, a_class):
    """ returns True if the object is an instance of,
    or if the object is an instance
    of a class that inherited from
    """

    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
