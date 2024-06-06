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
        list_dicts = []

        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            if list_objs is None:
                json.dump(list_dicts, f)
            else:
                for obj in list_objs:
                    if isinstance(obj, cls):
                        obj_dict_rep = obj.to_dictionary()
                        list_dicts.append(obj_dict_rep)
                serialized_str = Base.to_json_string(list_dicts)
                data = json.loads(serialized_str)
                pretty_json_str = json.dumps(data)
                json.dump(data, f)
