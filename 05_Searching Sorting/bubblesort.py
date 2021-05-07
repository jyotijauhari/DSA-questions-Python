from  sys import  stdin
def takeinput():
    n = int(stdin.readline().strip())

    if n==0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr,n

# not optimised
# def bubblesort(arr, n):
#     for i in range(0,n):
#         for j in range(1,n):
#             if arr[j-1] > arr[j]:
#                 arr[j-1], arr[j] = arr[j],arr[j-1]
#             else:
#                 continue

#  optimised
def bubblesort(arr, n):
    for i in range(0,n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
            else:
                continue
#main
arr, n = takeinput()
# print(arr)
# print(n)

bubblesort(arr,n)
print(arr)