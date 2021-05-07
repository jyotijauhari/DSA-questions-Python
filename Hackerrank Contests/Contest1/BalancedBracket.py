#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    bracket = {"(" :")", "{":"}", "[":"]"}
    ip = ["(", "{", "[" ]
    for char in s:
        if char in ip:
            stack.append(char)
        else:
            if stack:
                top = stack.pop()
                if bracket[top] != char:
                    return "NO"
            else:
                return "NO"
    if stack:
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
