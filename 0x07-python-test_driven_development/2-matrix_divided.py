#!/usr/bin/python3
"""Defines the function `matrix_divided`"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix"""
    new_matrix = []
    matrix_len = len(matrix)
    if not all(isinstance(i, list) for i in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    for row in matrix:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
    if matrix_len > 1:
        for i in range(matrix_len + 1):
            if len(matrix[i]) != len(matrix[i+1]):
                raise TypeError("Each row of the matrix must have "
                                "the same size")
            break
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    """The actual division of the matrix"""
    for row in matrix:
        new_row = []
        for elem in row:
            new_row.append(round(elem / div, 2))
        new_matrix.append(new_row)

    return new_matrix
