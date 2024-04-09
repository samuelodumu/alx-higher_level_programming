#!/usr/bin/python3
"""Module with a square class"""


class Square:
    """defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Instantiation of objects"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 1 or value[1] < 1:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """To print the square using '#'"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                position = list(self.__position)
                for j in range(self.__size):
                    while position[0] > 0:
                        print(" ", end='')
                        position[0] -= 1
                    print("#", end='')
                print()
