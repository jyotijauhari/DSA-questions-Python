class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.key = k


def height(root):
    if root == None:
        return 0
    else:
        lh = height(root.left)
        rh = height(root.right)
        return max(lh, rh) + 1


# Driver Code

root = Node(100)
root.left = Node(200)
root.right = Node(300)
root.right.left = Node(400)

print(height(root))
