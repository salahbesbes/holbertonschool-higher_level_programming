#!/usr/bin/python3
""" no module """


class Rectangle:
    """ create rectangle """
    def __init__(self, width=0, height=0) -> None:
        """ init class

            args:
                width(int) : width
                height(int) :height
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ get width """
        return self.__width
    @width.setter
    def width(self, value):
        """set width

        Args:
            value (int): set widtha
        """
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ get height  """
        return self.__height

    @height.setter
    def height(self, value):
        """set height

        Args:
            value (int): height
        """
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculate area  """
        return self.__height * self.__width

    def perimeter(self):
        """ calculate perimatre """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width + self.__height) * 2
    