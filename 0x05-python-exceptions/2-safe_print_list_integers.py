#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    counter, loop = 0, 0
    while loop < x:
        try:
            print("{:d}".format(my_list[loop]), end='')
            counter += 1
            loop += 1
        except (TypeError, ValueError):
            loop += 1
    print()
    return counter
