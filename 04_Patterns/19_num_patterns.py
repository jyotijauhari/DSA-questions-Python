'''
1234
123
12
1

i = n
j = n - i + 1
val = j then j ++
'''

n = 4
i = 1
while(i<=n):
    j = 1
    while( j<= (n - i + 1) ):
        print(j, end=" ")
        j += 1
    print()
    i += 1