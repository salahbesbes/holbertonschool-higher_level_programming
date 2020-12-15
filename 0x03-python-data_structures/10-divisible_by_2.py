#!/usr/bin/python3


def divisible_by_2(my_list=[]):

    new_list = [(my_list[i] % 2) == 0 for i in range(len(my_list))]
    return new_list
