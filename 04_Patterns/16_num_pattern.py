'''
1
21
321
4321

i = n
j = i
val = i , then i -- (take dummy var)
'''

n = 4
i = 1
while(i<=n):
    p = i
    j = 1
    while(j<=i):
        print(p, end=" ")
        p -= 1
        j += 1
    print()
    i += 1