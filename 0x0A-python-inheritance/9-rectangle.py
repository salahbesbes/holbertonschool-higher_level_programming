#!/usr/bin/python3
""" module """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ class geo """

    def __init__(self, width, height):
        """ init class """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ docstring for __str__ """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        return self.__height * self.__width
