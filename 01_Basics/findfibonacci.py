'''
print fibonaci
fib(2) = 1
011235
'''
def findfib(n):
    f = 0
    s = 1
    if n == 0 :
        return  0
    if n == 1:
        return 1
    for i in range(2,n+1):
        next = f + s
        f = s
        s = next
    return next

print(findfib(5))

