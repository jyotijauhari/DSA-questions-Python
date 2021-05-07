# arr = [1,2,1,5,1]

def search(arr, n, l, h):

    if l > h or h == 0 or h == -1:
        return -1
    if arr[l] == n:
        return l

    return search(arr, n, l+1, h)

arr = [1,2,1,4,2,1]
h = len(arr) - 1
l = 0
n = 6
idx = search(arr, n, l, h)
print("{} is present at {} location" .format(n, idx ))