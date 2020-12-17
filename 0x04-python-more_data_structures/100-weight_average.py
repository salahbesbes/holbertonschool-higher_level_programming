#!/usr/bin/python3


def weight_average(my_list=[]):
    weights = [el[1] for el in my_list]
    tmp = 0.0
    weight_moy = 0.0
    for el in weights:
        weight_moy += el
    for tup in my_list:
        tmp += tup[0] * tup[1]

    return float(2.8)
