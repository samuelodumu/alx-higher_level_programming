#!/usr/bin/python3
"""Contains `class_to_json` function"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    serialized_dict = {}

    attributes = obj.__dict__

    # Iterate over each attribute

    for attr in attributes:
        attr_name = attr
        try:
            attr_value = getattr(obj, attr)
        except Exception:
            continue

        if type(attr_value) is list:
            serialized_list = []

            for item in attr_value:
                if is_instance_of_class(item):
                    serialized_list.append(class_to_json(item))
                else:
                    serialized_list.append(item)
            serialized_dict[attr_name] = serialized_list

        elif type(attr_value) is dict:
            sub_dict = {}

            for key, value in attr_value.items():
                if is_instance_of_class(value):
                    serialized_dict[key] = class_to_json(value)
                else:
                    sub_dict[key] = value
            serialized_dict[attr_name] = sub_dict

        elif isinstance(attr_value, (str, bool, int)):
            serialized_dict[attr_name] = attr_value

    return serialized_dict


def is_instance_of_class(value):
    return not isinstance(value, (int, str, list, dict, bool))
