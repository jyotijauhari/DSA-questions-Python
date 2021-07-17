from math import inf


class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.key = k


def getMax(root):
    if root == None:
        return -inf
    else:
        lm = getMax(root.left)
        rm = getMax(root.right)

        return max(root.key, lm, rm)


# Driver Code

root = Node(100)
root.left = Node(200)
root.right = Node(105)
root.right.left = Node(400)
root.right.right = Node(500)

print(getMax(root))
