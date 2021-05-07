# 5 4 3 2 1
def prntNaturalNum(n):
    if n==0:
        return 0
    prntNaturalNum(n-1)
    print(n, end=" ")
    return



prntNaturalNum(5)