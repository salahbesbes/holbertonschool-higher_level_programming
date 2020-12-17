#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):

    if key not in a_dictionary:
        a_dictionary[key] = value
        return a_dictionary

    for k, val in a_dictionary.items():
        if k == key:
            a_dictionary[k] = value
            return a_dictionary
