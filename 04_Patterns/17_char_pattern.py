'''
A
BC
CDE
DEFG

i = n
j = i
value =  chr(65+i-1)  = for first char of each row
v2 = chr( ord(value) + j - 1) = for all rem char of row
'''
n = 4
i = 1
while(i<=n):
    value = chr(65+i-1)
    j = 1
    while(j<=i):
        v2 = chr( ord(value) + j - 1)
        print(v2, end =" ")
        j += 1
    print()
    i += 1