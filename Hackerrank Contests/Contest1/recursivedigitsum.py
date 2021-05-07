# n = "123"
# k = 2
# print(n*k)
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def superdigit(stri):
    if len(stri) == 1:
        return int(stri)
    else:
        # first = int(stri[0])
        # return first + superdigit(stri[1:])
        new_num = str(sum([int(i) for i in stri]))
        return superdigit(new_num)

def superDigit(n, k):
    final_digit = n * k
    return superdigit(final_digit)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
