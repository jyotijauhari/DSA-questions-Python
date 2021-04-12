
def findele(arr,n):
    if len(arr) == 0:
        return False
    num = arr[0]
    if num == n:
        return True
    return findele(arr[1:], n)

arr = [5,6,7,8]
print(findele(arr,1))
