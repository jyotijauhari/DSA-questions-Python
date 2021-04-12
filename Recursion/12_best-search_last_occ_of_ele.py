def search(arr, n, si):
    l = len(arr)
    if si == l:
        return -1
    smallerListOutput = search(arr, n, si+1)

    if smallerListOutput != -1:
        return smallerListOutput
    else:
        if arr[si] == n:
            return si
        else:
            return -1

print(search([1,1,1,1,2], 1, 0))