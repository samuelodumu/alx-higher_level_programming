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
