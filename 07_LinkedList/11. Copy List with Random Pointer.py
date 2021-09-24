"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# Without hashmap, space complexity little less but overall O(N) space, O(N) time
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        cur = head
        copyHead = Node(-1)
        copyCur = copyHead
        
        #create copy list and use zigzag order
        while cur:
            copyCur.next = Node(cur.val)
            nextCur = cur.next
            cur.next = copyCur.next
            copyCur.next.next = nextCur
            cur = nextCur
        #verifying that zigzag worked
        #cur = head
        #while cur:
        #    print(cur.val)
        #    cur = cur.next
        
        #connect the randoms
        cur = head
        while cur:
            #The random is either None or exists
            if cur.random:
                #random is not None so set copy.random to orig.random.next
                cur.next.random = cur.random.next
            #if it's None then we don't have to do anything bc copy.random is none by default
                
            cur = cur.next.next
        
        #split up into two linked lists
        cur = head
        copyCur = copyHead
        while cur:
            copyCur.next = cur.next
            cur = cur.next.next
            copyCur = copyCur.next           
        
        return copyHead.next

# O(N) space, O(N) time using hashmap

# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         origToCopy = {} #map each orig node its respective copy node
        
#         copyHead = Node(-1) #dummy head node 
#         copyCur = copyHead
#         cur = head
        
#         #do iteration to create copyList without the randoms first (so we can fill up the dictionary)
#         while cur:
#             copyCur.next = Node(cur.val)
            
#             #map new node pair, and advance the pointers
#             origToCopy[cur] = copyCur.next
#             cur = cur.next
#             copyCur = copyCur.next
        
#         #iterate through linked list again and now assign random pointers
#         cur = head
#         copyCur = copyHead
#         while cur:
#             #get the copyRandom
#             origRandom = cur.random
#             if origRandom:
#                 copyRandom = origToCopy[origRandom]
#             else:
#                 copyRandom = None
                
#             #assign the random pointer
#             copyCur.next.random = copyRandom
            
#             #advance the pointers
#             cur = cur.next
#             copyCur = copyCur.next
            
#         return copyHead.next
        
    
