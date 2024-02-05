#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    x = []
    for i in range(2):
        if not tuple_a:
            x.append(tuple_b[i])
            break
        elif not tuple_b:
            x.append(tuple_a)
            break
        elif not tuple_a and tuple_b:
            x.append(0)
            break
        elif len(tuple_a) == i:
            x.append(tuple_b[i])
        elif len(tuple_b) == i:
            x.append(tuple_a[i])
        elif len(tuple_a) and len(tuple_b) == i:
            x.append(0)
        else:
            x.append(tuple_a[i] + tuple_b[i])
    new_tuple = tuple(x)
    return new_tuple
