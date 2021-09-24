# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        forw = None
        
        while curr:
            forw = curr.next #next
            curr.next = prev #link
            
            prev = curr
            curr = forw
        
        return prev
            