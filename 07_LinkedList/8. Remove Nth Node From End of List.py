# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://www.youtube.com/watch?v=Lhu3MsXZy-Q
# 2 iteration 2 pointer approach O(2n)

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return None
        if not head.next.next:
            if n == 1:
                head.next = None
                return head
            elif n == 2:
                return head.next
        # find the length of the list
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        # edge case: only remove first node
        if length == n:
            return head.next
        # iterate through list using slow and fast pointers
        slow = head
        fast = head.next
        for i in range(length - n - 1):
            slow = fast
            fast = fast.next
        # remove nth to last node
        slow.next = fast.next
        fast.next = None
        # return head of the list
        return head
    
    
    
# fast and slow pointer approach O(n)
# class Solution:    
# 	def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
# 		dummy=ListNode(0)
# 		dummy.next=head
# 		slow=fast=dummy
        
# 		for i in range(n):
# 			fast=fast.next
            
# 		while fast.next:
# 			fast=fast.next
# 			slow=slow.next
            
# 		slow.next=slow.next.next
# 		return dummy.next
        
    
