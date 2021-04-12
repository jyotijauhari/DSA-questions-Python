# arr = [1,2,3,4,5]

def sorted(arr, si):
    l = len(arr)
    if si == l - 1 or l == 1 :
        return True
    if (arr[si] > arr[si + 1]):
        return False
    return sorted(arr, si + 1)


print(sorted([1,2,3,4,4,5], 0))