#!/usr/bin/python3
"""Contains the `BaseGeometry` class"""


class BaseGeometry:
    """Contains `area` function"""
    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates `value`"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
