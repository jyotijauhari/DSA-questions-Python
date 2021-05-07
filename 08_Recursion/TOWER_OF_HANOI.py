# def towerofhanoi(n,a,b,c):
#     if n==1:
#         print("move 1st disk from ", a , " to " ,c)
#         return
#     towerofhanoi(n-1,a,c,b)
#     print("move ", n, "th disk from", a, " to ", c)
#     towerofhanoi(n-1, b,a,c)
#
# towerofhanoi(3,"source", "helper", "intermediate")

"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""

import sys

sys.path.append("..")  # Adds higher directory to python modules path.
from trace_recursion import trace


def towers_of_hanoi(n, a, b, c):
    if n == 1:
        print("Move disk 1 from source", a, "to destination", c)
        return
    towers_of_hanoi(n - 1, a, c, b)
    print("Move disk", n, "from source", a, "to destination", c)
    towers_of_hanoi(n - 1, b, a, c)


n = 3
towers_of_hanoi = trace(towers_of_hanoi)
# A, C, B are the names of the rods.
# They correspond to source, destination, auxiliary
towers_of_hanoi(n, 'A', 'B', 'C')