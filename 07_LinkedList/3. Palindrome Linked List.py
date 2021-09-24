# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# brute force - O(n2) by using two ptr , one at start other at end
# time complexity - O(n)

class Solution:
    
    def middleNode(self, head: ListNode) -> ListNode:
        temp = head
        while temp and temp.next:
            head = head.next
            temp = temp.next.next
        return head
    
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
    
    def isPalindrome(self, head: ListNode) -> bool:
        
        if head == None or head.next == None:
            return True
        
        midnode = self.middleNode(head)
        nHead = self.reverseList(midnode)
        
        c1 = head
        c2 = nHead
        
        res = True
        while(c2!=None):
            if c1.val != c2.val :
                res = False
                break
            c1 = c1.next
            c2 = c2.next
            
        nHead = self.reverseList(nHead)
        head.next = nHead
        
        return res
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        