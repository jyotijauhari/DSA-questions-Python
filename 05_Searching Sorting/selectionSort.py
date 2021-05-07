from  sys import  stdin
def takeinput():
    n = int(stdin.readline().strip())

    if n==0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr,n


def selectionsort(arr, n):
    for i in range(0,n):
        min = i
        for j in range(i+1, n):
            if arr[j]<arr[min]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]

#main
arr, n = takeinput()
selectionsort(arr,n)
print("sorted list is : ", arr)
# print(arr)
# print(n)


