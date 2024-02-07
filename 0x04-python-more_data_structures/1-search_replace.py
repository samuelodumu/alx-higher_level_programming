#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_list = my_list.copy()

    if search not in my_list:
        return my_list
    else:
        x = new_list.count(search)
        for i in range(x):
            idx = new_list.index(search)
            new_list.remove(search)
            new_list.insert(idx, replace)
        return new_list
