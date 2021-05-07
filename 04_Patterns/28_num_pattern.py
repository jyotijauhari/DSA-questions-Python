'''
   1
  232
 34543
4567654

   1
  23
 345
4567

i = n

for spaces
j = n - i : print spaces

for number
j = i
p = i
print(p)
p++

   1
  232
 34543
4567654

for decreasing
j = i - 1
value = 2*(i-1) then i--
(use diff var like p)
'''

n = 4
i = 1
while(i<=n):
    j = 1
    while(j<=n-i):
        print(" ", end=" ")
        j += 1

    j = 1
    p = i
    while(j<=i):
        print(p, end=" ")
        p += 1
        j += 1

    j = 1
    p = 2*(i-1)
    while(j<=i-1):
        print(p, end=" ")
        p -= 1
        j += 1

    print()
    i += 1