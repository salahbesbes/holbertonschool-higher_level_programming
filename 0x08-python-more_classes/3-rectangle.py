#!/usr/bin/python3
""" no module """


class Rectangle:
    """ create rectangle """
    def __init__(self, width=0, height=0) -> None:
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        return self.__height * self.__width
    
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width + self.__height) * 2
        
    def __str__(self) -> str:
        res = ""
        for row in range(self.__height):
            res += '#' * self.__width
            res += '\n'
        return res[:len(res) - 1]