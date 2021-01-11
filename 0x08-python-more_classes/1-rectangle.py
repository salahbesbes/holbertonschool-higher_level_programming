#!/usr/bin/python3
""" no module """


class Rectangle:
    """ create rectangle """
    def __init__(self, width=0, height=0) -> None:
        """init Class

        Args:
            width (int, optional): width. Defaults to 0.
            height (int, optional): height. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width """
        return self.__width

    @width.setter
    def width(self, value):
        """set width

        Args:
            value (int): width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ get height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height

        Args:
            value (int): height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value