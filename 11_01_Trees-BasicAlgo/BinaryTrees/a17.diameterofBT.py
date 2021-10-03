def height(root):
    if root == None:
        return 0
    return 1 + max(height(root.right), height(root.left))
        
def diameter(root):
    if root == None:
        return 0
    
    option1 = height(root.left) + height(root.right)
    option2 = diameter(root.left)
    option3 = diameter(root.right)
    
    return max(option1, option2, option3)