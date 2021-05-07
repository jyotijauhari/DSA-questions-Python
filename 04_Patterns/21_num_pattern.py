'''
n = 4
1 #never consider this
11
121
1221

****
11
121
1221
****

n = 4
print("1")
i = n-1
j = i + 1
val = if (j == 1 or j == i+1 ) -> print(1)
else print(2)
'''

n = int(input("enter n: "))
i = 1
print(1)
while(i <= n-1):
    j = 1
    while(j<=i+1):
        if j==1 or j== i+1:
            print(1, end=" ")
        else:
            print(2, end=" ")
        j += 1
    print()
    i += 1

