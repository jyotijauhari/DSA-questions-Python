# brute force - find max ele in array by max function or traversal - O(N)
# O(logn) - binary search

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        low = 0
        high = len(arr) - 1

        while low < high:
            mid = (low + high) // 2

            if arr[mid] >= arr[mid + 1]:
                high = mid
            else:
                low = mid + 1
        return low