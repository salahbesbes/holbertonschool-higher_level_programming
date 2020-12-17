#!/usr/bin/python3


def best_score(a_dictionary):
    if (a_dictionary is None or a_dictionary == {}):
        return None
    scores = [val for key, val in a_dictionary.items()]
    scores.sort()
    return scores[-1]
