def sumofele(li):
    if len(li) == 1:
        return li[0]
    return li[0] + sumofele(li[1:])

arr = [1,2,3,40]
print(sumofele(arr))