#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    length = len(my_list) - 1
    check = []

    for i in range(length):
        if my_list[i] % 2 == 0:
            check.append(True)
        else:
            check.append(False)

    return check
