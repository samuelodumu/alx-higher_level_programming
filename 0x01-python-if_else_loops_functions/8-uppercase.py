#!/usr/bin/python3
def uppercase(str):
    result = ''
    for i in str:
        if ord(i) in range(97, 123):
            result += chr(ord(i) - 32)
        else:
            result += i
    print('{}'.format(result), end='\n')
