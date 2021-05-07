#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
# 0 0 1 0 0 1 1 0 , k = 2
def jumpingOnClouds(c, k):
    n = len(c)
    e = 100
    i = 0
    # for i in range(k,n,k):
    #     if c[i] == 0:
    #         count -= 1
    #     elif c[i] == 1:
    #         count -= 3
    # return count
    while (1):
        if c[i] == 0:
            e -= 1
        elif c[i] == 1:
            e -= 3
        i = (i + k) % n
        if i == 0:
            break
    return e


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
