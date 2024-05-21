#!/usr/bin/python3
"""Contains lookup function"""


def lookup(obj):
    """Returns a list of all attributes and methods in 'obj'"""
    return dir(obj)
