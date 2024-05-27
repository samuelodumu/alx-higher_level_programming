#!/usr/bin/python3
"""Contains `append_write` function"""


def append_write(filename="", text=""):
    """appends `text` to `filename`"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
