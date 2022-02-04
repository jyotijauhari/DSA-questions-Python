def factorial(n):
    if n==0:
        return 1
    #small_next = factorial(n-1)
    #n,small_next
    #return n*small_next
    return n*factorial(n-1)

print(factorial(5))


# def fact(n, ans):
#     if n == 1:
#         print(ans)
#         return
    
#     ans *= n
#     fact(n-1, ans)
    
#     # TODO: write code...



# n = 5
# fact(n,1)
