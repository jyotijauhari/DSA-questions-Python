def sort(arr):
    if len(arr) == 1:
        return arr
        
    temp = arr.pop()
    sort(arr)
    insert(arr, temp)
    return arr
    

def insert(arr, temp):
    if len(arr)==0 or arr[len(arr)-1]<=temp:
        arr.append(temp)
        return arr
        
    temp1 = arr.pop()
    insert(arr, temp)
    arr.append(temp1)
    return arr


arr = [5,1,0,2]

print(sort(arr))
