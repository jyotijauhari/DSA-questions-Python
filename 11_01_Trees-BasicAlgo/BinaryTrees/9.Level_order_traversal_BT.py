# deque is used as priority queue in python
from collections import deque

class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.key = k


def printLevelOrder(root):
    if root is None:
        return

    q = deque()
    q.append(root)

    while len(q) > 0:
        node = q.popleft()
        print(node.key)

        if node.left is not None:
            q.append(node.left)

        if node.right is not None:
            q.append(node.right)


# Driver code
root = Node(100)
root.left = Node(200)
root.right = Node(300)
root.left.left = Node(400)
root.right.left = Node(500)
root.right.right = Node(600)
root.right.left.left = Node(700)
root.right.left.right = Node(800)

printLevelOrder(root)
