'''
ABCD
ABCD
ABCD
ABCD

i = n
j = n
number = 'A' + j - 1
ord, chr
 '''

n = 4
i = 1
while(i<=n):
    j = 1
    while(j<=n):
        print(chr(65+j-1), end=" ")
        j += 1
    print()
    i += 1


