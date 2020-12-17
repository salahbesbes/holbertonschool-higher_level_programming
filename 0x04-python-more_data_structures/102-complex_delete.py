#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    ar_to_del = []

    for k, val in a_dictionary.items():
        if (val == value):
            ar_to_del.append(k)

    for i in ar_to_del:
        a_dictionary.pop(i)
    return a_dictionary
