#!/usr/bin/pyhton3
"""Contains `read_file` function"""


def read_file(filename=""):
    """Reads the contents of a file"""
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    print(content, end="")
