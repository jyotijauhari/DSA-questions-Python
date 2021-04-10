def factorial(n):
    if n==0:
        return 1
    #small_next = factorial(n-1)
    #n,small_next
    #return n*small_next
    return n*factorial(n-1)

print(factorial(5))