#!/usr/bin/python3
""" module """
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """description"""

    def __init__(self, size):
        """ init class """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """docstring for __str__"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
