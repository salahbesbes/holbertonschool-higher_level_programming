#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for el in row:
            print("{:d}".format(el), end=" ")
        print()
