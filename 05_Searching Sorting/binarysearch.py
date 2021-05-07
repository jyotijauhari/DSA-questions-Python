# from  sys import  stdin
# def takeinput():
#     n = int(stdin.readline().strip())
#
#     if n==0:
#         return list(), 0
#     arr = list(map(int, stdin.readline().strip().split(" ")))
#     return arr,n
# #main
# arr, n = takeinput()
# print(arr)
# print(n)

a = [1,2,3,4,5]
search = 9

start = 0
end = len(a) - 1
while start<=end :
    mid = (start+end)//2
    if a[mid] == search:
        print(mid)
        break
    elif a[mid] > search:
        end = mid - 1
    else:
        start = mid+1
else:
    print("not found")

