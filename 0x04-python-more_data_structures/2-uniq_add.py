#!/usr/bin/python3


def uniq_add(my_list=[]):
    summ = 0
    for el in (list(set(my_list))):
        summ += el
    return summ
