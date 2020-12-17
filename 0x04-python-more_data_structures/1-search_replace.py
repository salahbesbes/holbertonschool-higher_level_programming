#!/usr/bin/python3


def search_replace(my_list, search, replace):
    # def check(x):
    #    if (x == search):
    #        return replace
    #    return x
    # return list(map(check, my_list))
    # using comprehensition list
    return [el if el != search else replace for el in my_list]
