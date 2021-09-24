# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Dictionary/Hash table (time - O(n) space - O(n))
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dictionary = {}
        while head:
            if head in dictionary: 
                return True
            else: 
                dictionary[head]= True
            head = head.next
        return False
    
# Two pointers (time - O(n) space - O(1))
# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         if not head:
#             return False
#         slow = head
#         fast = head.next
#         while slow != fast:
#             if not fast or not fast.next:
#                 return False
#             slow = slow.next
#             fast = fast.next.next
#         return True
        