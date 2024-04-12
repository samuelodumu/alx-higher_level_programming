#!/usr/bin/python3
"""Module that supplies the function `add_integer`"""


def add_integer(a, b=98):
    """Function that adds two integers"""
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    result = a + b
    return result
