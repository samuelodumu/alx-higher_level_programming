#!/usr/bin/python3
"""Contains `save_to_json` function"""
import json


def save_to_json_file(my_obj, filename):
    """writes `my_obj` to `filename`, using a JSON representation"""
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
