class Solution(object):

    #### Main function

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [-1, -1]

        result[0] = self.findStartingIndex(nums, target)
        result[1] = self.findEndingIndex(nums, target)

        return result

    #### Helper function 1

    def findStartingIndex(self, nums, target):
        index = -1
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                index = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return index

    #### Helper function 2

    def findEndingIndex(self, nums, target):
        index = -1
        low, high = 0, len(nums) - 1

        while low <= high:

            mid = (low + high) // 2

            if nums[mid] == target:
                index = mid
                low = mid + 1  # 16
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return index