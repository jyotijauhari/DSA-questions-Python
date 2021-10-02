class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def treeInput():
        
    rootData = int(input())
    if rootData == -1:
        return None
    
    root = BinaryTreeNode(rootData)
    root.left = treeInput()
    root.right = treeInput()

    return root

def numLeafNodes(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    numLeafLeft = numLeafNodes(root.left)
    numLeafRight = numLeafNodes(root.right)
    
    return numLeafLeft + numLeafRight

root = treeInput()
print(numLeafNodes(root))