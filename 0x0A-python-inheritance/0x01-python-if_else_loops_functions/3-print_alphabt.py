#!/usr/bin/python3

for letter in range(ord('a'), ord('z') + 1):
    if letter != 113 and letter != 101:
        print('{}'.format(chr(letter)), end='')
