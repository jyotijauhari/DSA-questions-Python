'''
ABCD
BCDE
CDEF
DEFG

i = n
j = n
value = chr((ord('A') + i - 1 ) + j - 1 )
'''
n = 4
i = 1
while(i<=n):
    j = 1
    while(j<=n):
        val = chr((ord('A') + i - 1 ) + j - 1 )
        print(val, end =" ")
        j += 1
    print()
    i += 1