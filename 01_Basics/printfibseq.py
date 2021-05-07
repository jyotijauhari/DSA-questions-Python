def fib(n):
    a = []
    a.append(0)
    a.append(1)
    for i in range(2,n):
        next = a[i-1]+a[i-2]
        a.append(next)
    return a
print(fib(5))