#!/usr/bin/python3


class Square:
    """ private attr size """
    def __init__(self, size=0):
        self.__size = size

    def set_size(self, size):
        self.__size = size

    def get_size(self):
        return self.__size
