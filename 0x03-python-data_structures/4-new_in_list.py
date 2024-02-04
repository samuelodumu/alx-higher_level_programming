#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    x = len(new_list)
    if idx < 0:
        return new_list
    if idx >= x:
        return new_list
    del new_list[idx]
    new_list.insert(idx, element)
    return new_list
