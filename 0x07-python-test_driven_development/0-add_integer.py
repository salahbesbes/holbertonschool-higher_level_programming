#!/usr/bin/python3
""" no module 



"""


def add_integer(a, b=98):
    """ add 2 given integer
    
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if a + 1 == a or b + 1 == b:  # catch a value like 1e300
        raise OverflowError
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b

