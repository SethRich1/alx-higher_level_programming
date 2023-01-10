#!/usr/bin/python3

# islower - function that check for lowercase character
# Return - True ifEquals lowercase, if otherwise False

def islower(char):
    if (ord(char) > 96 and ord(char) < 123):
        return True
    else:
        False
