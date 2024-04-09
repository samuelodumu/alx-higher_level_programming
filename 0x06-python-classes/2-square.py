#!/usr/bin/python3
"""Module with a square class"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """Instantiation of objects"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
