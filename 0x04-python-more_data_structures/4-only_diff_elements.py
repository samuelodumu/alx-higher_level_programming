#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    common = list(set(set_1 ^ set_2))
    return common
