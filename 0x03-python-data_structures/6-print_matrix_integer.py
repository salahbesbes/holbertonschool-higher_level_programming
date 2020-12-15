#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        separator = ""
        for el in row:
            print(separator + "{:d}".format(el), end="")
            separator = " "
        print()
