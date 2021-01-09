#!/usr/bin/python3
""" no module """


def add_integer(a, b=98):
    """
    add_integer:
        Checks if parameters are int
        Returns sum of parameters
        
        raises:
            TypeError : if a or b is not int or float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

