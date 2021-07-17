class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.key = k


def treeSize(root):
    if root == None:
        return 0
    else:
        return 1 + treeSize(root.left) + treeSize(root.right)





# Driver Code

root = Node(7)
root.left = Node(8)
root.right = Node(9)
root.right.left = Node(10)
root.right.right = Node(11)

print(treeSize(root))
