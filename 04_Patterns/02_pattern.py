'''
Star pattern : 2
*
* * *
* * * * *
* * * * * * *
* * * * * * * * *
1-1
2-3
3-5
4-7
'''
k=1
for i in range(0,5):
    for j in range(0,k):
        print("*", end=" ")
    k+=2
    print()