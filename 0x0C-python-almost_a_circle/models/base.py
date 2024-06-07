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

        with open(f"{cls.__name__}.json", "w") as f:
            if list_objs is None:
                json.dump(list_dicts, f)
            else:
                # loop over each object in object list
                for obj in list_objs:
                    if isinstance(obj, cls):
                        # find the dictionary representation of the object
                        obj_dict_rep = obj.to_dictionary()
                        # appended them to list
                        list_dicts.append(obj_dict_rep)
                # serialized the list
                serialized_str = cls.to_json_string(list_dicts)
                # wrote serialized list to file
                f.write(serialized_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Square":
            demo = cls(5)
        elif cls.__name__ == "Rectangle":
            demo = cls(8, 4)

        demo.update(**dictionary)
        return demo

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        instances = []
        try:
            # open the file for reading
            with open(filename, 'r') as f:
                content_in_list = f.read()
                # convert JSON string `content_in_list` to python list
                list_dicts = cls.from_json_string(content_in_list)
                # create a class instance from each dict in the list
                for i in range(len(list_dicts)):
                    instance = cls.create(**list_dicts[i])
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []
