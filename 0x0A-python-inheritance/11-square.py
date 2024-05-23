#!/usr/bin/python3
"""Contains the `Square` class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Contains square functions"""
    def __init__(self, size):
        """Initializing attributes"""
        no_exception = True
        try:
            self.integer_validator("size", size)
        except Exception as e:
            no_exception = False
            print(f"[{e.__class__.__name__}] {e}")

        if no_exception:
            self.__size = size

    def area(self):
        """returns square area"""
        if self.__size == 0:
            return 0
        else:
            return self.__size ** 2

    def __str__(self):
        """returns a string representation"""
        return f"[Square] {self.__size}/{self.__size}"
