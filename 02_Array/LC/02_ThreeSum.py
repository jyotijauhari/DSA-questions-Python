# LC 15
class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res

# little complex
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
        
#         # base condition
#         if len(nums) < 3:
#             return []
        
#         nums.sort()
#         count = 0
#         i = 0
#         nums2 = nums
        
# #         while count < len(nums)-1:
# #             if nums[i] != nums[i+1]:
# #                 nums2.append(nums[i])
# #             i += 1
# #             count += 1
        

#         target = 0
#         ans = []
#         for i in range(len(nums2)):
#             l = i + 1
#             r = len(nums2) - 1
#             rem = target - nums2[i]
#             while l < r:
                
#                 if nums2[l] + nums2[r] == rem:
#                     ans.append([nums2[i], nums2[l], nums2[r]])
#                     l += 1
#                     r -= 1
                
#                 elif nums2[l] + nums2[r] > rem:
#                     r -= 1
                
#                 else:
#                     l +=1
                    
#         # removing duplicates from  ans 
#         s = set()
#         li = []
#         for i in ans:
#             ele = tuple(i)
#             if ele not in s:
#                 li.append(i)
#                 s.add(ele)
                
#         return li
                
                    
                
                
