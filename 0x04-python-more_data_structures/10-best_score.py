#!/usr/bin/python3


def best_score(a_dictionary):
    if (a_dictionary is None or a_dictionary == {}):
        return None
    best = 0
    name = ""
    for key, val in a_dictionary.items():
        if a_dictionary[key] >= best:
            best = a_dictionary[key]
            name = key
    return name
