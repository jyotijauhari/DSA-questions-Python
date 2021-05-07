'''
Star pattern : 1
*
* *
* * *
* * * *
* * * * *

'''

for i in range(0, 5):
    for j in range(0, 5):
        if j <= i:
            print("*", end=" ")
    print()

'''
for i in range(0, 5):
    for j in range(0, i+1):
        print("* ",end="")
    print()
'''