'''
ip - 123456, 3
op - 3
'''

def binarySearch(arr, s, e, ele):
    if s>e:
        return -1
    mid = (s+e)//2
    if arr[mid] == ele:
        return mid + 1   #as idx start from 0
    elif arr[mid] > ele:
        return binarySearch(arr, s, mid-1, ele)
    else:
        return binarySearch(arr, mid+1, e, ele)


print(binarySearch([1,2,3,4,5,6], 0, 5, 4))