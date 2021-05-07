'''
    1
   12
  123
 1234
12345

(row) i = n

for space
j = n -i
print("")

for num
j = i
print(p)
p++
'''

n = 5
i = 1
while(i<=n):
    j = 1
    while(j<=n-i):
        print(" ", end=" ")
        j += 1
    j = 1
    p = 1
    while(j<=i):
        print(p, end=" ")
        p += 1
        j += 1
    print()
    i += 1