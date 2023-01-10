#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    res = 0
    cnt = 1

    while cnt < len(argv):
        res += int(argv[cnt])
        cnt += 1
    print(res)
