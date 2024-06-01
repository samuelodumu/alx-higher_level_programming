#!/usr/bin/python3
"""Contains `Student` class"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Initializing attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves the dictionary representation of
        `Student` instance present in `attrs`"""
        selected_dict = {}
        # check if attrs is a list
        if type(attrs) is list:
            for item in attrs:
                # check if each item in the list is a string
                if Student.all_items_str(attrs):
                    for key, value in self.__dict__.items():
                        # check if the list item is in the dict
                        if item == key:
                            # add it to selected_dict
                            selected_dict[key] = value
                        else:
                            continue
                    return selected_dict
                else:
                    break
        return self.__dict__

    @staticmethod
    def all_items_str(some_list):
        for i in range(len(some_list)):
            if type(some_list[i]) is str:
                continue
            else:
                break
        if i == len(some_list) - 1:
            return True
        else:
            return False
