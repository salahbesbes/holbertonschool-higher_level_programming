#!/usr/bin/python3


def element_at(my_list, idx):
    length = len(my_list)
    if (idx >= 0 and idx <= length):
        return my_list[idx]
    else:
        return None
