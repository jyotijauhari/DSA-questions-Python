'''
    1
   121
  12321
 1234321
123454321

(row) i = n

for space
j = n -i
print("")

for num
j = i
print(p)
p++

for decreasing seq
j = i - 1
p = i
print(p-1)
p --

'''

n = 5
i = 1
while(i<=n):

    #starting spaces
    j = 1
    while(j<=n-i):
        print(" ", end=" ")
        j += 1

    # increasing seq
    j = 1
    p = 1
    while(j<=i):
        print(p, end=" ")
        p += 1
        j += 1

    # decreasing seq
    j = 1
    p = i
    while(j<=i-1):
        print(p-1,end=" ")
        p -= 1
        j += 1
    print()
    i += 1