#!/usr/bin/python3


def no_c(my_string):
    new_str = ''
    for char in my_string:
        if char == 'C':
            continue
        if char == 'c':
            continue
        else:
            new_str += char

    return new_str
