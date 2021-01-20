#!/usr/bin/python3
""" no module """


def pascal_triangle(n):
    """ create pascal triangle """
    pascal = []
    line = []
    for iteration in range(5):
        tmp = line[:]
        tmp.insert(0, 0)
        for i in range(iteration):
            line.append(i)
        line.append(1)
        zipped_lists = zip(tmp, line)
        sum = [x + y for (x, y) in zipped_lists]
        line = sum
        pascal.append(line[:])
    return pascal
