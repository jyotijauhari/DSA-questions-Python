def removeLeaves(root):
    if root == None:
        return None
    if root.left == None and root.right == None:
        return None
    root.left = removeLeaves(root.left)       
    root.right = removeLeaves(root.right)
    
    return root
