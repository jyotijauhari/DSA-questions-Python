# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# bit manipulation
# class Solution(object):
#     def getDecimalValue(self, head):
#         """
#         :type head: ListNode
#         :rtype: int
#         """
#         ans = 0
#         while head:
#             ans = ans << 1
#             ans =  ans + head.val 
#             head = head.next
#         return ans
            
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        answer = 0
        while head: 
            answer = 2*answer + head.val 
            head = head.next 
        return answer 
        