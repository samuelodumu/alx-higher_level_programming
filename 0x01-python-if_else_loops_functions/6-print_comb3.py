#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            break
        print('{}{}'.format(i,  j), end=', ')
print('{}'.format(89))
