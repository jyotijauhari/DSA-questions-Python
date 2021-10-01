# LC 845
# time - O(N) space - O(1)
class Solution(object):
        def longestMountain(self, A):
            res = up = down = 0
            for i in range(1, len(A)):
                if down and A[i - 1] < A[i] or A[i - 1] == A[i]: up = down = 0
                up += A[i - 1] < A[i]
                down += A[i - 1] > A[i]
                if up and down: res = max(res, up + down + 1)
            return res

# time - O(N2) almost, space - O(1)
#     def longestMountain(self, arr):
#         """
#         :type arr: List[int]
#         :rtype: int
#         """
        
#         longestpeak = 0
#         if len(arr) <= 2:
#             return 0
        
#         i = 1
#         while i < len(arr)-1:
#             isPeak = arr[i-1] < arr[i] and arr[i] > arr[i+1]
#             if not isPeak:
#                 i += 1
#                 continue
                
#             leftidx = i - 1
#             while leftidx >= 0 and arr[leftidx] < arr[leftidx+1]:
#                 leftidx -= 1
            
            
#             rightidx = i + 2
#             while rightidx <= len(arr)-1 and arr[rightidx] < arr[rightidx-1]:
#                 rightidx += 1
                
#             currentmax = rightidx - leftidx - 1
#             if currentmax > longestpeak:
#                 longestpeak = currentmax
#             i = rightidx
#         return longestpeak
            
            
