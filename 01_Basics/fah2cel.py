# c = (f - 32 ) * 5/9

# li = [1,2,3,4,5,6]
# for i in li[1:5]:
#     print(i)

# n = int(input())
# li = []
# for i in range(n):
#     li.append(int(input()))
# print(li)

#space sep input

#way1
# n = int(input())
#
# str = input()
# str_split = str.split(" ")
# li = []
# for i in str_split:
#     li.append(int(i))
# print(li)

#way 2
li = [int(x) for x in input().split()]
print(li)