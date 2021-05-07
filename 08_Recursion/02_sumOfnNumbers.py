def sum(n):
    if n==0:
        return 0
    # small_op = sum(n-1)
    # return n + small_op
    return n+sum(n-1)

print(sum(5))