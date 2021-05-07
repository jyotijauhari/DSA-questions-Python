def reversearr(arr, i, j):
    while i<j:
        arr[i] ,arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr


def rotateR(d, arr):
    # reverse helper function
    arr = reversearr(arr, 0, len(arr)-1)
    arr = reversearr(arr, 0, d-1)
    arr = reversearr(arr, d+1, len(arr)-1)
    return arr

print(rotateR(4, [1,2,3,4,5]))