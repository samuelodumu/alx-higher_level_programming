#!/usr/bin/python3

def add_num(*args, **kwargs):
    num = 0
    if len(args) == 0:
        for key, value in kwargs.items():
            num = value
        return num
    else:
        for arg in args:
            num += arg
        return num


print(add_num(2, number=82))

print(add_num(1, 3, 4, 5, sam=72))
