#!/usr/bin/python3
"""Contains empty class `Rectangle`"""


class Rectangle:
    """defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        if type(value) is not int:
            raise TypeeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
