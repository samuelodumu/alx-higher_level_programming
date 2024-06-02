#!/usr/bin/python3
"""Contains `pascal_triangle` function"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the
    Pascal’s triangle of n"""
    if n <= 0:
        return []
    else:
        pascal_triangle = []

        for i in range(n):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(pascal_triangle[i - 1][j - 1]
                               + pascal_triangle[i - 1][j])
            pascal_triangle.append(row)

        return pascal_triangle
