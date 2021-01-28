#!/usr/bin/python3
""" modules """
Base = __import__("base").Base


class Rectangle(Base):
    """description"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init class """
        super(Rectangle, self).__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def id(self):
        """ getter id """
        return self.__id

    @id.setter
    def id(self, id):
        """ setter id """
        if type(id) is not int:
            raise TypeError("id must be an integer")
        self.__id = id

    @property
    def width(self):
        """ getter width"""
        return self.__width

    @width.setter
    def width(self, width):
        """ setter for width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ getter height"""
        return self.__height

    @height.setter
    def height(self, height):
        """ setter for height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ getter x"""
        return self.__x

    @x.setter
    def x(self, x):
        """ setter for x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ getter y"""
        return self.__y

    @y.setter
    def y(self, y):
        """ setter for y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        return self.__height * self.__width

    def display(self):
        """ print reclangle of shome char default '#'
        """
        res = ""
        if self.__height == 0 or self.__width == 0:
            return res
        for i in range(self.__y):
            res += '\n'
        for row in range(self.__height):
            res += ' ' * self.__x + '#' * self.__width
            res += '\n'
        print(res[:len(res) - 1])

    def __str__(self):
        """
        print instance
        :return: string
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(str(self.__id),
                                                       str(self.__x),
                                                       str(self.__y),
                                                       str(self.__width),
                                                       str(self.__height))

    def update(self, *args, **kwargs):
        """
            update all attribute either args or kwargs by passing
            then to their own setter
            but when a new att is given its set the class.__dict__
        :param self:
        :param args: id, width, height, x, y
        :param kwargs: only if args is empty
        """
        attrs = vars(self)  # dict of attrs
        if not args:  # if args is empty (args == None -> not empty)
            # passing new values to the setter
            for key, val in kwargs.items():
                if "_Rectangle__" + key in attrs.keys():
                    self.__setattr__(key, val)
        else:
            # create new dict from the tuple
            keys = attrs.keys()
            zipped_lists = zip(keys, args)
            new_attrs = {str(key): arg for (key, arg) in zipped_lists}
            # check for errors
            # cleaning '_Rectangle__'
            new_attrs = {key[12:]: val for key, val in new_attrs.items()}
            # passing new values to the setter
            for key, val in new_attrs.items():
                self.__setattr__(key, val)

    def to_dictionary(self):
        """
            return new dict of attributes
        :return: dicts
        """
        attrs = vars(self)  # dict of attrs
        # removing '_Rectangle__'
        return {key[12:]: val for key, val in attrs.items()}
