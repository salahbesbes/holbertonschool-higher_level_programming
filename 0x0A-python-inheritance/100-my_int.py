#!/usr/bin/python3
""" no module """


class MyInt(int):
    """ class MyInt """

    def __init__(self, val):
        """ class init """
        self.val = val

    def __eq__(self, o: object) -> bool:
        return self.val != o

    def __ne__(self, x: object) -> bool:
        return self.val == x
