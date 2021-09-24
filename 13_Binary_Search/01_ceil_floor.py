# ceil of number
# 1 2 3 4 5 6 
#number - 2

def findceil(arr, num):
    start = 0
    end = len(arr) - 1 
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == num:
            return mid
        elif arr[mid] >= num:
            end = mid - 1 
        else:
            start = mid + 1 
    return start
    
def findfloor(arr, num):
    start = 0
    end = len(arr) - 1 
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == num:
            return mid
        elif arr[mid] >= num:
            end = mid - 1 
        else:
            start = mid + 1 
    return end
    
# arr = list(map(int, input().split()))
# num = int(input())
arr = [2,3,5,9,14,16,18]
num = 15
print(findceil(arr, num))
print(findfloor(arr, num))
