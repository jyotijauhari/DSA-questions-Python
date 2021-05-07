def partition(arr, s, e):
    pivot = arr[s]
    #find no of ele smaller than pivot
    c = 0
    for i in range(s,e+1):
        if arr[i] < pivot:
            c+=1
        arr[s+c] , arr[s]  = arr[s], arr[s+c]
        pivot_idx = s+c

        i = s
        j = e

        while i < j:
            if arr[i] < pivot:
                i += 1
            elif arr[j] >= pivot:
                j -= 1
            else:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        return pivot_idx

def quicksort(arr, s, e):
    if s >= e:
        return
    pivot_idx = partition(arr, s, e)
    quicksort(arr, s, pivot_idx - 1)
    quicksort(arr, pivot_idx+1, e)

    return arr

print(quicksort([1,2,4,12,3,6], 0, 5))