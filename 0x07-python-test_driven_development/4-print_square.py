#!/usr/bin/python3
"""Contains print_square function"""


def print_square(size):
    """prints a square according to the 'size' parameter"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
