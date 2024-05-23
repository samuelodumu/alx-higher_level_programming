#!/usr/bin/python3
"""Contains the `Rectangle` class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        no_exception = True
        try:
            self.integer_validator("width", width)
        except Exception as e:
            print(f"[{e.__class__.__name__}] {e}")
            no_exception = False

        if no_exception:
            self.__width = width

        try:
            self.integer_validator("height", height)
        except Exception as e:
            print(f"[{e.__class__.__name__}] {e}")
            no_exception = False

        if no_exception:
            self.__height = height

    def area(self):
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
