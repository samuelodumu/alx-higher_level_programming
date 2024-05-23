#!/usr/bin/python3
"""Contains the `Square` class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Contains square functions"""
    def __init__(self, size):
        """Initializing attributes"""
        Rectangle.__init__(self, size, size)

    def area(self):
        """returns square area"""
        return Rectangle.area(self)
