'''
alpha pattern -

A
BB
CCC
DDDD

i = n
j = i
val = chr(65+j-1)
'''

n = 4
i = 1
while(i<=n):
    j = 1
    while(j<=i):
        val = chr(65+i-1)
        print(val, end=" ")
        j += 1
    print()
    i += 1