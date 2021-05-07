def isSorted(li):
    if len(li) == 0 or len(li) == 1 :
        return True
    if li[0] > li[1]:
        return False
    newli = li[1:]
    isSmallerListSorted = isSorted(newli)
    if isSmallerListSorted:
        return True
    else:
        return False

list = [5,6,7,8]
print(isSorted(list))