#!/usr/bin/python3

for num in range(0, 9):
    for num_1 in range(1, 10):
        if num < num_1:
            if num == 8:
                print("{}{}".format(num, num_1))
            else:
                print("{}{},".format(num, num_1), end=" ")
