#!/usr/bin/python3
"""Contains `Rectangle` class"""


class Rectangle:
    """defines a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializing width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
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
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.height == 0:
            return 0
        else:
            result = (self.__width * 2) + (self.__height * 2)
            return result

    def __str__(self):
        if self.__width == 0 or self.height == 0:
            return f""
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    print(f"{self.print_symbol}", end="")
                if i < self.__height - 1:
                    print()
            return ""

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
