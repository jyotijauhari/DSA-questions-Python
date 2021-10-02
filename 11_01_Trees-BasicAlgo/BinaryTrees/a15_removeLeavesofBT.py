def removeLeaves(root):
    if root == None:
        return None
    if root.left == None and root.right == None:
        return None
    root.left = removeLeaves1(root.left)       
    root.right = removeLeaves1(root.right)
    
    return root
