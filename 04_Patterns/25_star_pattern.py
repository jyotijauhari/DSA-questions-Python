'''
    *
   **
  ***
 ****
*****

i = n
for space
j =  n - i
value = " "

for stars
j = i
value = " * "
'''

n = 5
i = 1
while(i<=n):
    j = 1
    while(j<=n-i):
        print(" ", end = " ")
        j += 1
    j = 1
    while(j <= i):
        print("*", end=" ")
        j += 1
    print()
    i += 1
