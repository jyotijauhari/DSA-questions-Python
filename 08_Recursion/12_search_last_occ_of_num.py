def search(arr, n):
    l = len(arr)
    if l == 0:
        return -1

    smallerList = arr[1:]
    smallerListOutput = search(smallerList, n)

    if smallerListOutput != -1:
        return smallerListOutput + 1
    else:
        if arr[0]  == n :
            return 0
        else:
            return -1


print(search([1,2,2,3,40], 2))