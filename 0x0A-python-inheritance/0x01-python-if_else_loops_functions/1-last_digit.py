#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = abs(number) % 10
if number < 0:
    num = -num
print("Last digit of {} is {} and is ".format(number, num), end="")
if num > 5:
    print("greater than 5")
elif num == 0:
    print("0")
else:
    print("less than 6 and not 0")
