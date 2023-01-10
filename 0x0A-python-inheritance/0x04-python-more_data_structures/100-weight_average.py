#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    score = 0
    weight = 0
    for x, y in my_list:
        score += (x * y)
        weight += y
    return score / weight
