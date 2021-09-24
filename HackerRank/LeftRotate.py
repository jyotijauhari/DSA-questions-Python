# easy method

def rotateLeft(d, arr):
    # reverse helper function
    return (arr[d:] + arr[0:d])


# n space n time
def rotateLeft(d, arr):
    n = len(arr)
    newarr = [None] * n

    for i in range(n):
        newidx = (i + n - d) % n
        newarr[newidx] = arr[i]

    return newarr


# d space n time
# function to rotate array by d elements using temp array
def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr

# O(1) space , O(n*d) time

# Function to left rotate arr[] of size n by d*/
def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)


# Function to left Rotate arr[] of size n by 1*/
def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp

# O(1) space, O(n) time ( gcd method )
def leftRotate(arr, d, n):
    for i in range(gcd(d, n)):

        # move i-th values of blocks
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

def gcd(a, b):
    if b == 0:
        return a;
    else:
        return gcd(b, a%b)
