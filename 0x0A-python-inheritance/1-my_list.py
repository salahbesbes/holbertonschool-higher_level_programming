#!/usr/bin/python3
""" no module  """


class MyList(list):
    """ my list class  """

    def print_sorted(self):
        """ print sort list """
        new = self[:]
        new.sort()
        print(new)
