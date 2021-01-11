#!/usr/bin/python3
""" no module """


class Rectangle:
    """ create rectangle """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0) -> None:
        """ init class

            args:
                width(int) : width
                height(int) :height
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self) -> str:
        """ print instance """
        res = ""
        if self.__height == 0 or self.__width == 0:
            return res
        for row in range(self.__height):
            res += str(self.print_symbol) * self.__width
            res += '\n'
        return res[:len(res) - 1]

    def __repr__(self) -> str:
        """ use of repr() """
        return "{}({}, {})".format(__class__.__name__,
                                   self.__width, self.__height)

    def __del__(self):
        """ del instance """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """check for bigger rect

        Args:
            rect_1 (Rectangle): fist rec
            rect_2 (Rectangle): last rec
        """
        if not isinstance(rect_1, __class__):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, __class__):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
