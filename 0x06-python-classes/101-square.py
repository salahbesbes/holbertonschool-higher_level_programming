#!/usr/bin/python3
""" empty module """


class Square:
    """ private attr size """
    def __init__(self, size=0, position=(0, 0)):
        """ init all attributes
        args:
            size (int): size of square
            position (int): tuple
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ getter size """
        return self.__size

    def position(self):
        """ getter position """
        return self.__size

    @size.setter
    def size(self, size):
        """ setter size
            Args:
                size(int): size of square
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def position(self, position):
        """ setter position
            Args:
                position(tuple): tuple
        """
        if isinstance(position, tuple) and len(position) == 2:
            if position[0] >= 0 and position[1] >= 0:
                self.__position = position
            else:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ calculate the area of the square """
        return self.__size * self.__size

    def my_print(self):
        """ print a square of # """
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__size + self.__position[0]):
                if j < self.__position[0]:
                    print(" ", end="")
                else:
                    print("#", end="")
            print()

        if self.__size == 0:
            print()

    def __repr__(self):
        """ print a square of # """
        result = ""
        for i in range(self.__position[1]):
            result += result.join('\n')
        for i in range(self.__size):
            for j in range(self.__size + self.__position[0]):
                if j < self.__position[0]:
                    result += result.join(' ')
                else:
                    result += result.join('#')
            if i != self.__size - 1:
                result += result.join('\n')

        if self.__size == 0:
            result += result.join('\n')
        return "{}".format(result)
