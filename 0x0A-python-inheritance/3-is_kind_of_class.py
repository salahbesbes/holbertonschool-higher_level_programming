#!/usr/bin/python3
""" no module """


def is_kind_of_class(obj, a_class):
    """ returns True if the object is an instance of,
    or if the object is an instance
    of a class that inherited from
    """
    if obj.__class__.__name__ == a_class.__name__:
        return True

    for base in obj.__class__.__bases__:
        if base.__name__ == a_class.__name__:
            return True
    return False
