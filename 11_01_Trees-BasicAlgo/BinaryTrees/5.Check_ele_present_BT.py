class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.key = k


def searchkey(root, key):
    if root is None:
        return False
    elif root.key == key:
        return True
    elif searchkey(root.left, key):
        return True
    else:
        return searchkey(root.right, key)


# Driver Code

root = Node(100)
root.left = Node(200)
root.right = Node(300)
root.right.left = Node(400)
root.right.right = Node(500)

print(searchkey(root, 100))
print(searchkey(root, 300))
print(searchkey(root, 350))
