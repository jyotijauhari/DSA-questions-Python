# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Brute Force - hashmap (dict)
# Algorithm-

# Take a hashset
# keep adding all nodes in hashset
# check if the current node alredy exists
# if it does than we are back at our starting loop (completed a round of circle) return the node
# After traversing the linkedlist if you are out of loop means no cycle!!!
# Space - O(N) , Time - O(N)


# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:
#         hashset=set()  # a set to store the visited nodes
#         while head:
#             if head in hashset:  #if node is already visited then we are back agin at start.
#                 return head
#             hashset.add(head)  
#             head=head.next
#         return None  #loop ends no cycle found

# Optimal Approach - two ptr
# Algorithm-

# Take two pointers and start from head.
# Move one pointer by 1 step and another by 2 steps.
# If at any point both pointers meet or collide means there is loop.
# Let one pointer remain on colliding position and take one on starting position.
# Move each pointer by 1 step now.
# Where ever the pointer collide it will be begning of our loop simply return
# Time Complexity - O(N)
# Space Complexity - O(1)

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow=head
        fast=head 
        flag=False 
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast: # Loop is detected mark flag as true
                flag=True
                break 
        if flag==False:  #if flag is false means there is no loop
            return None
        slow=head     #Let's go back to head of list
        while slow!=fast:  #loop until both pointers meet
            slow=slow.next 
            fast=fast.next
        return slow   #return any one of them

        