#!/usr/bin/python3
""" modules """
from .rectangle import Rectangle


class Square(Rectangle):
    """ class square """

    def __init__(self, size, x=0, y=0, id=None):
        """ init class square """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ string to print """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    @property
    def size(self):
        """ getter size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
            update attribute
        :param args: args
        :param kwargs: kwargs
        """
        # vars(self) => get all Square and parents attribute like this
        # {
        # 'id': 1, '_Rectangle__width': 2, '_Rectangle__height': 2,
        # '_Rectangle__x': 3, '_Rectangle__y': 0
        # }

        # vars(Square)
        # {
        # '__str__': <function Square.__str__ at 0x7f308e121b80>,
        # 'size': <property object at 0x7f308e153130>,
        # 'update': <function Square.update at 0x7f308e121d30> .....
        # }

        attrs = ["id", "size", "x", "y"]
        if not args:  # args is empty
            for key, val in kwargs.items():
                setattr(self, key, val)
        else:
            zipped_lists = zip(attrs, args)
            zipped_lists = dict(zipped_lists)
            for key, val in zipped_lists.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """
            return new dict of attributes
        :return: dict of attributes in this class
        """
        attrs = vars(self)  # dict of attrs
        # removing '_Rectangle__'
        new_attrs = {key[12:]: val for key, val in attrs.items()}
        new_attrs.pop("width")  # removing width
        new_attrs.pop("height")  # removin height
        new_attrs["size"] = self.size  # adding size
        return new_attrs
