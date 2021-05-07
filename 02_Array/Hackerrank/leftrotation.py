# def rotateLeft(d, arr):
#     n = len(arr)
#     # Reverse the first `d` elements
#     reverse(arr, 0, d - 1)
#
#     # Reverse the remaining `n-d` elements
#     reverse(arr, d, n - 1)
#
#     # Reverse the whole array
#     reverse(arr, 0, n - 1)
#
#     return arr
#
#
# def reverse(arr, i, j):
#     while i < j:
#         arr[i], arr[j] = arr[j], arr[i]
#         i += 1
#         j -= 1
#     return arr

# one liner
def rotateLeft(d, arr):
    return (arr[d:] + arr[0:d])