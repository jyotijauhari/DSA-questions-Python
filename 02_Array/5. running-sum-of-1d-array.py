# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        init = nums[0]
        for i in range(1, len(nums)):
            nums[i] += init
            init = nums[i]
        return nums