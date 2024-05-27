#!/usr/bin/python3
"""Contains `to_json_string` function"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of `my_obj`"""
    return json.dumps(my_obj)
