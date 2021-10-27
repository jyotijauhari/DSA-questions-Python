# LC 590

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans=deque()
        if not root:
            return 
        stack=[root]
        while stack:
            a=stack.pop()
            ans.appendleft(a.val)
            for i in a.children:
                if i:
                    stack.append(i)
        return ans
