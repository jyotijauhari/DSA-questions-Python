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


'''
i = 0
n = 4
while i<n:
    j = 0
    val= 64 + n - i
    while j<=i:
        print(chr(val), end = "")
        val += 1
        j += 1 
    i += 1 
    print()
'''