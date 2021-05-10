class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printTree(root):
    if root == None:
        return
    print(root.data, end=" ")
    printTree(root.left)
    printTree(root.right)


def printdetailedTree(root):
    if root == None:
        return
    print(root.data, end=" : ")
    if root.left:
        print("L:", root.left.data, end=" ")
    if root.right:
        print("R:", root.right.data, end=" ")
    print()

    printdetailedTree(root.left)
    printdetailedTree(root.right)


def takeInput():
    rootData = int(input())
    if rootData == -1 :
        return None

    root = BinaryTreeNode(rootData)
    leftTree = takeInput()
    righttree = takeInput()
    root.left = leftTree
    root.right = righttree

    return root

def height(root):
    if root == None:
        return 0

    leftHeight = height(root.left)
    rightHeight = height(root.right)

    return 1 + max(leftHeight, rightHeight)

x = takeInput()
printdetailedTree(x)
print(height(x))