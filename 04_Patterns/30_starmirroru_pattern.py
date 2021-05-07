'''

    *
   ***
  *****
 *******
*********

n = 5
i= n

for space
j = n - i

for star till middle
    *
   **
  ***
 ****
*****
j = i
print *

for remaining mirror
j = i - 1
print(*)
'''

n = 5
i = 1
while(i<=n):
    j = 1

    #for spaces
    while(j<=n-i):
        print(" ", end=" ")
        j += 1
    j = 1

    #for starting stars
    while(j<=i):
        print("*", end=" ")
        j += 1
    j = 1

    #stars after mirror
    while(j<=i-1):
        print("*", end=" ")
        j += 1
    print()
    i += 1