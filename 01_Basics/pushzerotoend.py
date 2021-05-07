# n = int(input())
# arr = list(map(int,input().split()))
#
# for i in arr:
#     if i != 0:
#         print(i,end=" ")
# cnt = arr.count(0)
# print("0 "*cnt)


def pushZeroToEnd(arr):
    i = 0
    j = len(arr)-1
    while i < j:
        while i<j and arr[j]==0:
            j -= 1
        if arr[i] == 0:
            arr[i],arr[j] = arr[j],arr[i]
        i += 1

    return arr

arr = [1,0,0,4,0,0,1]
print(pushZeroToEnd(arr))
