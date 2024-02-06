#!/usr/bin/python3

def max_integer(my_list=[]):
    i = len(my_list)
    if i == 0:
        return None
    else:
        while i - 1 > 1:
            j = 0
            while j < i - 1:
                if my_list[j] > my_list[j + 1]:
                    temp = my_list[j]
                    my_list[j] = my_list[j + 1]
                    my_list[j + 1] = temp
                else:
                    pass
                j += 1
            i -= 1
        return my_list[-1]
