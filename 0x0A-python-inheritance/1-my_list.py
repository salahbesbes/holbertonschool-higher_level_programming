#!/usr/bin/python3
""" no module  """


class MyList(list):
    """ my list class  """

    def print_sorted(self):
        """ print sort list """
        self.sort()
        print(self)
