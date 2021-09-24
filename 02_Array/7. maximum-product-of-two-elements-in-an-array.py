# # nlogn
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)


# O(n)
class Solution(object):
    def maxProduct(self, nums):

        first, second = 0, 0

        for number in nums:

            if number > first:
                # update first largest and second largest
                first, second = number, first

            else:
                # update second largest
                second = max(number, second)

        return (first - 1) * (second - 1)