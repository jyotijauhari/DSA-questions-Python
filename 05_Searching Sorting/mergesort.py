'''
ip - [1,2,4,12,3,6]
op - [1,2,3,4,6,12]
'''


def merge(a1, a2, arr):
    i, j, k = 0, 0, 0
    while i < len(a1) and j < len(a2):
        if a1[i] <= a2[j]:
            arr[k] = a1[i]
            i += 1
            k += 1
        else:
            arr[k] = a2[j]
            j += 1
            k += 1

    while i < len(a1):
        arr[k] = a1[i]
        i += 1
        k += 1

    while j < len(a2):
        arr[k] = a2[j]
        j += 1
        k += 1

def mergeSort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return
    mid = len(arr)//2
    a1 = arr[0:mid]
    a2 = arr[mid:]
    mergeSort(a1)
    mergeSort(a2)
    merge(a1, a2, arr)
    return arr

print(mergeSort([1,2,4,12,3,6]))
