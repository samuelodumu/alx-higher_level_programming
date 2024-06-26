#!/usr/bin/python3
"""Contains `Square` class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Initializes attributes"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns string representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """Updates attributes"""
        if len(args) > 0:
            attrs = ["id", "size", "x", "y"]
            for i in range(min(len(args), len(attrs))):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in ["id", "size", "x", "y"]:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square instance"""
        dict_rep = {}
        attributes = ["id", "size", "x", "y"]
        for attribute in attributes:
            dict_rep[attribute] = getattr(self, attribute)
        return dict_rep
