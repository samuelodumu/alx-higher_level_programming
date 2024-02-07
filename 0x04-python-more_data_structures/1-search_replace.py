#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_list = my_list.copy()

    if search > len(my_list):
        return my_list
    else:
        new_list.insert(search - 1, replace)
        del new_list[search]
        return new_list
