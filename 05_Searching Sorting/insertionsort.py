from  sys import  stdin
def takeinput():
    n = int(stdin.readline().strip())

    if n==0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr,n

def insertionsort(arr,n):
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while(j>=0 and arr[j]>key):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key



#main
arr, n = takeinput()

insertionsort(arr,n)
print(arr)
