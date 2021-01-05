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
        self.size = size
        self.position = position

    @property
    def size(self):
        """ getter size """
        return self.__size

    @property
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

    @position.setter
    def position(self, position):
        """ setter position
            Args:
                position(tuple): tuple
        """
        if isinstance(position, tuple) and len(position) == 2 and \
                isinstance(position[0], int) and position[0] >= 0 and \
                isinstance(position[1], int) and position[1] >= 0:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ Calculate the area """
        return self.__size * self.__size

    def my_print(self):
        """ print a square of # """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
        for i in range(self.__size):
            for j in range(self.__size + self.__position[0]):
                if j < self.__position[0]:
                    print(" ", end="")
                else:
                    print("#", end="")
            print()
