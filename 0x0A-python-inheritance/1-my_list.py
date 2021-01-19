#!/usr/bin/python3
""" no module  """


class MyList(list):
    """ my list class  """

    def __init__(self):
        """ init class """
        super().__init__()

    def print_sorted(self):
        """ print sort list """
        self.sort()
        print(self)
