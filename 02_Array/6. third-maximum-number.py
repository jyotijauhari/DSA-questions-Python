# https://leetcode.com/problems/third-maximum-number/
# heapq is a binary heap, with O(log n) push and O(log n) pop . See the heapq source code. The algorithm you show takes O(n log n) 
# to push all the items onto the heap, and then O((n-k) log n) to find the kth largest element. So the complexity would be O(n log n).
import heapq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        S = []

        for x in set(nums):
            if len(S) < 3:
                heapq.heappush(S, x)
            else:
                heapq.heappushpop(S, x)

        return S[0] if len(S) == 3 else max(S)
