#!/usr/bin/python3


def check_empty(t1=(1, 2)):
    list1 = list(t1)
    len_t1 = len(t1)

    if len_t1 < 2:
        if len_t1 == 0:
            list1.append(0)
            list1.append(0)
        elif len_t1 == 1:
            list1.append(0)
        return (tuple(list1))
    return t1


def check_big_tuple(big_tuple=(1, 2, 3)):
    len_tuple = len(big_tuple)
    if len_tuple > 2:
        list_1 = list(big_tuple)[:2]
        return tuple(list_1)
    return big_tuple


def add_tuple(tuple_a=(), tuple_b=()):

    tuple_a = check_empty(tuple_a)
    tuple_a = check_big_tuple(tuple_a)

    tuple_b = check_empty(tuple_b)
    tuple_b = check_big_tuple(tuple_b)

    return tuple(map(sum, zip(tuple_a, tuple_b)))
