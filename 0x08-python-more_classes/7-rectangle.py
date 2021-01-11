#!/usr/bin/python3
""" no module """


class Rectangle:
    """ create rectangle """
    number_of_instances = 0
    print_symbol = '#'
    
    def __init__(self, width=0, height=0) -> None:
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        if self.__height == 0 or self.__width == 0:
            return res 
        for row in range(self.__height):
            res += str(self.print_symbol) * self.__width
            res += '\n'
        return res[:len(res) - 1]
    
    def __repr__(self) -> str:
        className = eval("self.__class__.__name__")
        height = str(eval("self.height"))
        width = str(eval("self.width"))
        return className + '(' + width  + ', ' + height + ')'
    
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        
    