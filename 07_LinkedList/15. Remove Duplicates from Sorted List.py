# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val :
                cur.next = cur.next.next
                continue
                
            cur = cur.next
        
        return head