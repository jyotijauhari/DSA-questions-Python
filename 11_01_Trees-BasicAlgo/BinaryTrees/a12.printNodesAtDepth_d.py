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

def printDepthd(root, d):
    
    if root == None:
        return 
    if d == 0:
        print(root.data)
        return 
    
    printDepthd(root.left, d-1)
    printDepthd(root.right, d-1)

root = treeInput()
d = int(input()) #depth
printDepthd(root, d)