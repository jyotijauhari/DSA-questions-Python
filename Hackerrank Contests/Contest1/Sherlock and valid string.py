#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
def getcount(li, val):
    count = 0
    for i in li:
        if i == val:
            count += 1
    return count


def isValid(s):
    dict = {}

    for char in s:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    # now have count of all char

    li = list(dict.values())
    max = 0
    min = 9999
    for count in li:
        if count >= max:
            max = count
        if count <= min:
            min = count

    count_min = getcount(li, min)
    count_max = getcount(li, max)
    # 55455 #5555 #54355 #22223
    if (count_min == 1 and count_max == len(li) - 1) or (count_min == 0 and count_max == len(li)) or (
            count_max == 1 and count_min == len(li) - 1):
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
