#!/usr/bin/python3
""" Module implementing Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ A class representing a rectangle with width
        and height, and spatial position x, y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instance initialization """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Getter of the private field width """
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter of the private field width
            Args:
                width: positive integer
        """

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ Getter of the private field height """
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter of the private field height
            Args:
                height: positive integer
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ Getter of the private field x """
        return self.__x

    @x.setter
    def x(self, x):
        """ Setter of the private field x
            Args:
                x: positive integer
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ Getter of the private field y """
        return self.__y

    @y.setter
    def y(self, y):
        """ Setter of the private field y
            Args:
                y: positive integer
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ Calculate and return the rectangle's area """
        return self.__height * self.__width

    def display(self):
        """ Prits to stdout the rectangle
            with the character '#'
        """
        print('\n' * self.__y, end="")
        for i in range(self.__height):
            print(' ' * self.__x, '#' * self.__width)

    def __str__(self):
        """ Return string representation of
            the rectangle
        """
        s = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return s.format(
                           self.id,
                           self.__x,
                           self.__y,
                           self.__width,
                           self.__height
                       )

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        if len(args):
            atts = ["id", "width", "height", "x", "y"]
            for k, v in zip(atts, args):
                setattr(self, k, v)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ Returning dictionary representation
            of instance attributes
        """
        atts = ["id", "width", "height", "x", "y"]
        return {k: getattr(self, k) for k in atts}
