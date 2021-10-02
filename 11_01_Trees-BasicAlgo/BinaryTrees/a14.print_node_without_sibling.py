class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def nodesWithoutSibling(root):
    if root == None:
        return 
    
    elif root.left is not None and root.right is not None:
        nodesWithoutSibling(root.left)
        nodesWithoutSibling(root.right)
    
    elif root.right is not None:
        print(root.right.data)
        nodesWithoutSibling(root.right)
        
    elif root.left is not None:
        print(root.left.data)
        nodesWithoutSibling(root.left) 