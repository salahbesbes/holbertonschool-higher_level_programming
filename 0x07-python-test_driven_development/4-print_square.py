#!/usr/bin/python3
""" no module """


def print_square(size):
    """ print square

    Args:
        size (int): size

    Raises:
        TypeError: [size must be an integer]
        ValueError: [size must be >= 0]
    """
    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")
    if size < 0:
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        raise ValueError("size must be >= 0")
    for row in range(int(size)):
        print('#' * int(size))