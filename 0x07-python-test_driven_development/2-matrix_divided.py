#!/usr/bin/python3
""" no module """

def matrix_divided(matrix, div):
    
    """ create matrix

    Args:
        matrix (list): list of list of integer
        div (int): division number

    Raises:
        TypeError: [matrix must be a matrix (list of lists) of integers/floats]
        TypeError: [Each row of the matrix must have the same size]
        TypeError: [div must be a number]
        ZeroDivisionError: [division by zero]

    Returns:
        [list]: [new list of lists of integer]
    """
    rowlength = 0
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i, row in enumerate(matrix):
        if not isinstance(row, list):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if i > 0:
            if len(matrix[i - 1]) != len(matrix[i]):
                raise TypeError("Each row of the matrix must have the same size")
        for el in row:
            if not isinstance(el, int) and not isinstance(el, float):
               raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")       
    return [[round(el / div, 2) for el in row] for row in matrix]


        