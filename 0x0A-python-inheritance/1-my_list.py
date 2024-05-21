#!/usr/bin/python3
"""Contains MyList class"""


class MyList(list):
    """A list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        new_list = self.copy()
        if len(new_list) == 0:
            return []
        for i in range(len(new_list) - 1):
            if new_list[i] > new_list[i + 1]:
                tmp = new_list[i]
                new_list[i] = new_list[i + 1]
                new_list[i + 1] = tmp
        print(new_list)
