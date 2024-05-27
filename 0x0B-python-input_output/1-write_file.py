#!/usr/bin/python3
"""Contains `write_file` function"""


def write_file(filename="", text=""):
    """writes `text` to `filename`"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
