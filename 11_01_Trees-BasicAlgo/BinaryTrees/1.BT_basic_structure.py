class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.key = k


# Driver Code

root = Node(5)
root.left = Node(4)
root.right = Node(2)
root.left.right = Node(3)
