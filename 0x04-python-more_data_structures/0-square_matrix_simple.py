#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    # using list comprehention
    # return [[el ** 2 for el in row] for row in matrix]
    # using map
    def power(x): return pow(x, 2)
    newMatrix = []
    for lst in matrix:
        newMatrix.append(list(map(power, lst)))
    return newMatrix
