class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def countNodesGreaterThanX(root, x):
    if root == None:
        return 0
    
    leftX = countNodesGreaterThanX(root.left, x)
    rightX = countNodesGreaterThanX(root.right, x)
            
    if root.data > x:
        return 1 + leftX + rightX
    return leftX + rightX 