# https://leetcode.com/problems/increasing-triplet-subsequence/submissions/
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
                # second = float('inf')
            elif n <= second:
                second = n
            else:
                return True
        return False

