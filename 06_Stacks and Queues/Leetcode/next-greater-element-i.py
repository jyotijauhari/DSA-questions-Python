# Brute force
# class Solution:
#     def nextGreaterElement(self, nums1, nums2):
#
#         result = []
#
#         for i in nums1:
#             flag = False
#             value = i
#             idx = nums2.index(value)
#
#             for j in range(idx, len(nums2)):
#
#                 if nums2[j] > value:
#                     result.append(nums2[j])
#                     flag = True
#                     break
#
#             if flag is False:
#                 result.append('-1')
#
#         return result

# Optimised
# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         if not nums2:
#             return None
#
#         mapping = {}
#         result = []
#         stack = []
#         stack.append(nums2[0])
#
#         for i in range(1, len(nums2)):
#             while stack and nums2[i] > stack[-1]:  # if stack is not empty, then compare it's last element with nums2[i]
#                 mapping[stack[-1]] = nums2[
#                     i]  # if the new element is greater than stack's top element, then add this to dictionary
#                 stack.pop()  # since we found a pair for the top element, remove it.
#             stack.append(
#                 nums2[i])  # add the element nums2[i] to the stack because we need to find a number greater than this
#
#         for element in stack:  # if there are elements in the stack for which we didn't find a greater number, map them to -1
#             mapping[element] = -1
#
#         for i in range(len(nums1)):
#             result.append(mapping[nums1[i]])
#         return result


#more optimised
class Solution:
    def nextGreaterElement(self, A: List[int], B: List[int]) -> List[int]:
        stack = []
        diff = {}

        for pos, val in enumerate(B):

            while stack and stack[-1] < val:
                diff[stack.pop()] = val

            stack.append(val)

        for pos in range(len(A)):

            if A[pos] in diff:
                A[pos] = diff[A[pos]]
            else:
                A[pos] = -1

        return A

nums1 = [4,1,2]
nums2 = [1,3,4,2]
ans = Solution()
print(ans.nextGreaterElement(nums1,nums2))