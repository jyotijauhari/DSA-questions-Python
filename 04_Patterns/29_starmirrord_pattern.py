'''

*********
 *******
  *****
   ***
    *

i = n

for space
j = i - 1

*****
 ****
  ***
   **
    *
for left triangle
j = n - i + i

*****.****
 ****.***
  ***.**
   **.*
    *.
for remaining
j = n - i

'''
n = 5
i = 1
while(i<=n):
    j = 1
    while(j<=i-1):
        print(" ", end=" ")
        j += 1

    j = 1
    while(j<= n-i+1):
        print("*", end=" ")
        j += 1

    j = 1
    while(j<= n-i):
        print("*", end=" ")
        j += 1
    print()
    i += 1