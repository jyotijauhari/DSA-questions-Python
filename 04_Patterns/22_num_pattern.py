'''
12344321
123**321
12****21
1******1


1234 4321
123* *321
12** **21
1*** ***1

i = n
j = n
val1 =
if j <= n-i+1
print(j)
else
print(*)

4321
*321
**21
***1

i = n
j = 0
if j <= i - 1
print *
else
print(n-j)



'''

n = 4
i = 1
while(i<=n):
    j = 1
    while(j<=n):
        if (j<=n-i+1):
            print(j, end=" ")
        else:
            print("*", end=" ")
        j += 1
    
    j = 1 
    while(j<=n):
        if (j<= i - 1):
            print("*", end=" ")
        else:
            print(n-j+1, end=" ")
        j += 1
    print()
    i += 1
