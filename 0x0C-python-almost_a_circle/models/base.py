#!/usr/bin/python3
"""Contains `base` class"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of `list_dictionaries`"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return f"[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of `list_objs` to a file"""
        for obj in list_objs:
            to_json_string(obj)
        with open(f"{cls}.json", "w", encoding="utf-8"):
            if list_objs is None:
                f"{cls}.json".write("[]")
            else:
                json.dump(list_objs, f"{cls}.json")
