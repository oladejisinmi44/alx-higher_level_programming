#!/usr/bin/python3

"""
This module supplies the function matrix_divided.
Used to perform scalar division of a matrix.
"""


def matrix_divided(matrix, div):
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    elif len(matrix) != 0:
        if not isinstance(matrix[0], list):
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        else:
            for i in matrix:
                if len(i) == 0:
                    raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
                for j in i:
                    if not isinstance(j, (int, float)):
                        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    else:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    a = len(matrix)
    if a == 0:
        return
    if a >= 2:
        for x in range(1, len(matrix)):
            if len(matrix[x]) != len(matrix[x - 1]):
                raise TypeError("Each row of the matrix must have \
the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    new = [[round(z / div, 2) for z in y] for y in matrix]
    return new
