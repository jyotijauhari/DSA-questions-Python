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
 321
  21
   1
i = n
j = n-i+1



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
    print()
    i += 1
