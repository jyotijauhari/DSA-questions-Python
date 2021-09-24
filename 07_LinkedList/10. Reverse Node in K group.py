# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    th, tt = None, None
    
    def calculate_length(self, head:ListNode) -> int:
        n_elem = 0
        while head is not None:
            n_elem += 1
            head = head.next
            
        return n_elem
    
    def addFirst(self, node: ListNode):
        if self.th == None:
            self.th = node
            self.tt = node
        else:
            node.next = self.th
            self.th = node
        
        
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        if head == None or head.next == None or k == 0:
            return head
        
        length = self.calculate_length(head)
        
        curr = head
        oh, ot = None, None #original head, tail
        
        while (length >= k):
            tempK = k 
            while(tempK ):
                forw = curr.next
                curr.next = None
                self.addFirst(curr)
                curr = forw
                tempK -= 1
                
            if oh == None:
                oh = self.th
                ot = self.tt
            else:
                ot.next = self.th
                ot = self.tt
            
            self.th, self.tt = None, None
            length -= k
            
        ot.next = curr
        return oh
            
        