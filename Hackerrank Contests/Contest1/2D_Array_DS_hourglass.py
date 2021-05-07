#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_sum = -63  # as -9*7
    # max hour glasses = 16 [6*6 grid ]
    for i in range(4):
        for j in range(4):
            firstrow = sum(arr[i][j:j + 3])
            middlerow = arr[i + 1][j + 1]
            lastrow = sum(arr[i + 2][j:j + 3])

            hourglass_sum = firstrow + middlerow + lastrow
            max_sum = max(max_sum, hourglass_sum)
    return max_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
