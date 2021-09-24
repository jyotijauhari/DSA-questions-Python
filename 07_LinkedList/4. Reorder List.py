# class Solution:

#     def middleNode(self, head: ListNode) -> ListNode:
#         temp = head
#         while temp and temp.next:
#             head = head.next
#             temp = temp.next.next
#         return head
    
#     def reverseList(self, head: ListNode) -> ListNode:
#         prev = None
#         curr = head
#         forw = None
        
#         while curr:
#             forw = curr.next #next
#             curr.next = prev #link
            
#             prev = curr
#             curr = forw
        
#         return prev
    
#     def reorderList(self, head: ListNode) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """

#         midnode = self.middleNode(head)

#         nHead = midnode.next
#         midnode.next = None

#         nHead = self.reverseList(nHead)

#         c1 = head
#         c2 = nHead
#         t1 = None
#         t2 = None
        
#         while c1 and c2:
#             t1, t2 = c1.next, c2.next
#             c1.next = c2
#             c2.next = t1
#             c1, c2 = t1, t2

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        f, s = head, head

        while f and f.next:
            f = f.next.next
            s = s.next

        f = s.next
        s.next = None

        node = None

        while f:
            t = f.next
            f.next = node
            node = f
            f = t
        while head and node:
            t1, t2 = head.next, node.next
            head.next = node
            node.next = t1
            head, node = t1, t2
