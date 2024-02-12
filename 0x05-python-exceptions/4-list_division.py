#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result = []
    count = 0

    while count < list_length:
        try:
            result.append(my_list_1[count] / my_list_2[count])
        except ZeroDivisionError:
            print('division by 0')
            result.append(0)
            continue
        except TypeError:
            print('wrong type')
            result.append(0)
            continue
        except IndexError:
            print('out of range')
            result.append(0)
            continue
        finally:
            count += 1
    return result
