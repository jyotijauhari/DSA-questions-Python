# 5 4 3 2 1
def prntNaturalNum(n):
    if n == 0:
        return
    print(n)
    prntNaturalNum(n-1)