def getHeightAndCheckBalanced(root):
    if root == None:
        return 0, True
    
    lh, isLeftBalanced = getHeightAndCheckBalanced(root.left)
    rh, isRightBalanced = getHeightAndCheckBalanced(root.right)
    
    h = 1 + max(lh, rh)
    
    if lh - rh > 1 or rh - lh > 1:
        return h, False
    
    if isLeftBalanced and isRightBalanced:
        return h, True
    else:
        return h, False
'''      
def height(root):
    if root == None:
        return 0

    return 1 + max(height(root.left), height(root.right))
    
def isBalanced(root):
    if root == None:
        return True      # Because Empty tree is balanced
    
    lh = height(root.left)
    rh = height(root.right)
    if lh - rh > 1 or rh - lh > 1:
        return False
    
    isLeftBalanced = isBalanced(root.left)
    isRightBalanced = isBalanced(root.right)
    
    if isLeftBalanced and isRightBalanced:
        return True
    else:
        return False

'''  