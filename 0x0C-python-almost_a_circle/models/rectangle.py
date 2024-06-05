#!/usr/bin/python3
"""Contains `Rectangle` class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """returns the rectangle's area"""
        return self.__width * self.__height

    def display(self):
        """displays the rectangle"""
        if self.__x > 0 or self.__y > 0:
            for a in range(self.__y):
                print()
            for i in range(self.__height):
                for b in range(self.__x):
                    print(" ", end="")
                for j in range(self.__width):
                    print("#", end="")
                print()
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    print("#", end="")
                print()

    def __str__(self):
        """returns string representation"""
        return (
            f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
            f"{self.__width}/{self.__height}"
        )

    def update(self, *args, **kwargs):
        """Updates id, width, height, x and y values"""
        if len(args) == 0:
            for key, value in kwargs.items():
                if key in ["id", "width", "height", "x", "y"]:
                    setattr(self, key, value)
        else:
            kwargs = None
            args_len = len(args)
            attrs = ["id", "width", "height", "x", "y"]

            for i in range(min(len(attrs), args_len)):
                setattr(self, attrs[i], args[i])
