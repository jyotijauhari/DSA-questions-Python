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


# def takeInput():
#     rootData = int(input())
#     if rootData == -1 :
#         return None
#
#     root = BinaryTreeNode(rootData)
#     leftTree = takeInput()
#     righttree = takeInput()
#     root.left = leftTree
#     root.right = righttree
#
#     return root

#level order input
def takeInput():

    rootData = int(input())

    if rootData == -1 :
        return None

    root = BinaryTreeNode(rootData)
    root.left = takeInput()
    root.right = takeInput()

    return root

x = takeInput()
printdetailedTree(x)