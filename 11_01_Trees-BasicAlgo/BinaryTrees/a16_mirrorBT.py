# simple swapping

def mirrorBinaryTree(root):
    if root == None:
        return None
    
    if root.left == None and root.right == None:
        return None
    
    mirrorBinaryTree(root.left)
    mirrorBinaryTree(root.right)
        
    temp = root.left
    root.left = root.right
    root.right = temp        

    return root
