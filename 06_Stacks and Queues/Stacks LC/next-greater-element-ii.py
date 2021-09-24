#https://leetcode.com/problems/next-greater-element-ii

# Brute force O(N2)
# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
#
#         ans = []
#
#         n = len(nums)
#
#         nums1 = nums.copy()
#
#         nums.extend(nums1)
#         print(nums)
#
#         for i in range(len(nums)):
#
#             flag = 0
#             for j in range(i + 1, len(nums)):
#
#                 if nums[i] < nums[j]:
#                     flag = 1
#                     ans.append(nums[j])
#                     break
#
#             if flag == 0:
#                 ans.append(-1)
#
#             if len(ans) == n:
#                 break
#
#         return ans

#time - O(n) and space - O(n)
# 2pass method
# time N and space N
class Solution:
    def nextGreaterElements(self, A: List[int]) -> List[int]:

        result = [-1] * len(A)
        stack = []

        for pos, val in enumerate(A):
            while stack and val > A[stack[-1]]:
                result[stack.pop()] = val
            stack.append(pos)

        for pos, val in enumerate(A):
            while stack and val > A[stack[-1]]:
                result[stack.pop()] = val

        return result

x = Solution()
print(x.nextGreaterElements([1,2,1]))