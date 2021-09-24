# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(1) space, O(n) time
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        odd = head
        even = head.next
        initial_even = even
        
        x = even.next 
        
        while x:
            temp = x
            even.next = x.next
            even = even.next
			
            odd.next = temp
            odd = odd.next
			
            x= even.next if even else None
            
        odd.next = initial_even
        
            
        return head
        