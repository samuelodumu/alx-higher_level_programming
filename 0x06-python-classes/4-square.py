#!/usr/bin/python3
"""Module with a square class"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """Instantiation of objects"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        """To calculate the area of the square"""
        return self.__size**2
