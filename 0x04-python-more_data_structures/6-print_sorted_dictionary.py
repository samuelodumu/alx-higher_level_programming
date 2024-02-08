#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    tup_items = tuple(a_dictionary.items())
    sorted_tup = sorted(tup_items, key=lambda x: x[0])
    sorted_dict = dict(sorted_tup)

    for i in sorted_dict.items():
        print("{} : {}".format(i[0], i[1]))
