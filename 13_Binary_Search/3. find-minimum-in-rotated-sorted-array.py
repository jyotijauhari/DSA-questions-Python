# log(n)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            if nums[mid] < nums[0]:
                high = mid
            else:
                low = mid + 1

        if nums[low] < nums[0]:
            return nums[low]
        else:
            return nums[0]
