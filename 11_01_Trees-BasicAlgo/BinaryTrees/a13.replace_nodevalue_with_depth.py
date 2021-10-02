class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to insert nodes in level order
def insertLevelOrder(arr, root, i, n):
    # Base case for recursion
    if i < n:
        temp = BinaryTreeNode(arr[i])
        root = temp
        # insert left child
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)
        # insert right child
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)
    return root
 
# Function to print tree nodes in
# InOrder fashion
def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.data,end=" ")
        inOrder(root.right)

def replaceWithDepth(root,level=0):
    if root == None:
        return 
    if root.data is not None:
        root.data = level
    replaceWithDepth(root.left, level + 1)
    replaceWithDepth(root.right, level + 1)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, root, 0, n)
    replaceWithDepth(root)
    inOrder(root)