#!/usr/bin/python3
""" empty module """


class Square:
    """ private attr size """

    def __init__(self, size=0):
        """ init all attributes
        args:
            size (int): size of square
        """
        self.__size = size

    @property
    def size(self):
        """ getter size """
        return self.__size

    @size.setter
    def size(self, size):
        """ setter size
            Args:
                size(int): size of square
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ calculate the area of the square """
        return self.__size * 2

    def __eq__(self, o) -> bool:
        return self.area() == o.area()

    def __ne__(self, o) -> bool:
        return self.area() != o.area()

    def __lt__(self, object):
        return self.area() < object.area()

    def __le__(self, object):
        return self.area() <= object.area()

    def __gt__(self, object):
        return self.area() > object.area()

    def __ge__(self, object):
        return self.area() >= object.area()
