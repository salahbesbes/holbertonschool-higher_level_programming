#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """docstring for safe_print_list

    : print safe list
    : return nb of element printed

    """
    i = 0
    try:
        while i < x:
            print(my_list[i], end="")
            i += 1
        print()
        return i
    except Exception:
        print()
        return i
