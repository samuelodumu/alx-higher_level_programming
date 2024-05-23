#!/usr/bin/python3
"""Contains the `Rectangle` class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    no_exception = True

    def __init__(self, width, height):
        try:
            self.integer_validator("width", width)
        except Exception as e:
            print(f"{e}")
            self.no_exception = False

        if self.no_exception:
            self.__width = width

        try:
            self.integer_validator("height", height)
        except Exception as e:
            print(f"{e}")
            self.no_exception = False

        if self.no_exception:
            self.__height = height
