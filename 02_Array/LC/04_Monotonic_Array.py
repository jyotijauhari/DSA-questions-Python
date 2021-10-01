# LC 896
class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        Increasing = True
        Decreasing = True
        
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                Decreasing = False
            if nums[i] < nums[i-1]:
                Increasing = False
        return Increasing or Decreasing
            
