'''
D
CD
BCD
ABCD

i = n
j = i
val = chr( 65 + n - i)  = first char of each row
v2 =  chr( ord(val) + j - 1) ) = rem char of row
'''

n = 4
i = 1
while(i<=n):
    val = chr(65 + n - i)
    j = 1
    while(j<=i):
        v2 = chr( ord(val) + j - 1)
        print(v2, end= " ")
        j += 1
    print()
    i += 1