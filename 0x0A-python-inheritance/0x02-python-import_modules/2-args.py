#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    ac = len(argv) - 1

    if ac == 0:
        print('{} arguments.'.format(ac))
    else:
        if ac == 1:
            print('{} argument:'.format(ac))
        else:
            print('{} arguments:'.format(ac))
        for i in range(1, ac + 1):
            print('{}: {}'.format(i, argv[i]))
