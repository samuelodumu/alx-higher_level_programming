#!/usr/bin/python3
"""Contains MyList class"""


class MyList(list):
    """A list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        new_list = self.copy()
        n = len(new_list)
        if n == 0:
            print("[]")
        else:
            for i in range(n):
                for j in range(n - i - 1):
                    if new_list[j] > new_list[j + 1]:
                        new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
            print(new_list)
