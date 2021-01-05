#!/usr/bin/python3


class Square:
    """ define the size """
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def set_size(self, size):
        self.__size = size

    def get_size(self):
        return self.__size
