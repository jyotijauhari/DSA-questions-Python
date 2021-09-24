# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# heap/priority queue
# Time Complexity: O(n·log(m)) where n is the total number of elements and m is the number of lists
# Space Complexity: O(n)

# Approach:

# Take the first node of each of the linked lists
# and add it into a heap. When you add it to the heap
# add (node.val, i) where i is the ith list.

# Create a dummy node head.

# Pop the first node from the heap and make it the
# next node in the dummy-list. Remember to add the
# first node from the ith linked list into the heap
# since we just removed a node from this list from the heap.

# Repeat until the heap is empty.

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(None)
        curr = head
        h = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next
        
        while h:
            val, i = heapq.heappop(h)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next
        
        return head.next


# O(NlogK) 
# divide conquer technique
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
#         if not lists: # handle []
#             return None  
        
#         if len(lists) == 1:  # it can handle [[]], len([[]])=1
#             return lists[0] # return the nodes
        
#         if len(lists) == 2:
#             return self.merge2Lists(lists[0], lists[1])
        
#         left, right = 0, len(lists)-1
#         mid = (left+right) // 2
#         leftSide = lists[:mid]
#         rightSide = lists[mid:]
#         leftDone = self.mergeKLists(leftSide)
#         rightDone = self.mergeKLists(rightSide)
            
#         return self.merge2Lists(leftDone, rightDone)
        
        
#     def merge2Lists(self, list1, list2):
        
#         pre = dummy = ListNode('a')
        
#         while list1 and list2:
#             if list1.val <= list2.val:
#                 dummy.next = list1
#                 list1 = list1.next
#             else:
#                 dummy.next = list2
#                 list2 = list2.next
#             dummy = dummy.next 
        
        
#         if list1 and not list2:
#             dummy.next = list1

#         if not list1 and list2:
#             dummy.next = list2
        
#         return pre.next
        