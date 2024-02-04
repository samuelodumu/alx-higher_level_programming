#!/usr/bin/python3

import hidden_4
if __name__ == '__main__':
    func = dir(hidden_4)
    func.sort()
    for i in func:
        if i.startswith('__') == False:
            print('{}'.format(i))
