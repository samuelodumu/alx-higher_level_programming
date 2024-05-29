#!/usr/bin/python3
"""Contains `main` function"""
import json
import os
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """adds all arguments to a Python list, and then saves them to a file"""
    new_list = []
    filename = "add_item.json"

    if os.path.exists(filename):
        existing_list = load_from_json_file(filename)

        new_list = existing_list + sys.argv[1:]
        save_to_json_file(new_list, filename)

    else:
        new_list = new_list + sys.argv[1:]
        save_to_json_file(new_list, filename)

if __name__ == "__main__":
    main()
