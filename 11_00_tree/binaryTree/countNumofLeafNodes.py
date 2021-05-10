class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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

def numofLeafNodes(root):
    if root is None:
        return 0

    if root.left == None and root.right == None:
        return 1

    nleftleaf = numofLeafNodes(root.left)
    nrightleaf = numofLeafNodes(root.right)

    return nleftleaf + nrightleaf

x = takeInput()
printdetailedTree(x)
print(numofLeafNodes(x))