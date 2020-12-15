#!/usr/bin/python3


def no_c(my_string):
    tmp = my_string.translate({ord('c'): None})
    return tmp.translate({ord('C'): None})
