'''
n = 5
1
11
202
303
4004

print(1)
i = n - 1
j = i + 1
val = j == 1 or j == i + 1  - > print(i)
else print (0)

'''

n = int(input("enter num: "))
print(1)
i = 1
while(i <= n-1 ):
    j = 1
    while( j<= i+1):
        if j == 1 or j == i+1 :
            print(i, end=" ")
        else:
            print("0",end= " ")
        j += 1
    print()
    i += 1
