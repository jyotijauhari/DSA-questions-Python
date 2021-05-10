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
        print("L:",root.left.data, end=" ")
    if root.right:
        print("R:",root.right.data, end=" ")
    print()

    printdetailedTree(root.left)
    printdetailedTree(root.right)
# bt1 = BinaryTreeNode(1)
# bt2 = BinaryTreeNode(2)
# bt3 = BinaryTreeNode(3)
#
# bt1.left = bt2
# bt1.right = bt3
#
# printTree(bt1)

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

def countNumofNodes(root):
    if not root:
        return 0
    leftCount = countNumofNodes(root.left)
    rightCount = countNumofNodes(root.right)
    return  1 + leftCount + rightCount

def sumofNodes(root):
    if not root:
        return 0
    #root + sumofNodes(root.left) + sumofNodes(root.righ)

    leftdata = sumofNodes(root.left)
    rightdata = sumofNodes(root.right)

    return root.data + leftdata + rightdata

#Traversals
#inorder - left,root,right
def inorder(root):
    if not root:
        return None

    inorder(root.left)
    print(root.data, end= " ")
    inorder(root.right)

#preorder - root left right
def preorder(root):
    if not root:
        return None

    print(root.data, end = " ")
    preorder(root.left)
    preorder(root.right)

#postorder - left right root
def postorder(root):
    if not root:
        return None

    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")


def findmaxValue(root):
    if not root:
        return  -1

    leftLargest = findmaxValue(root.left)
    rightLargest = findmaxValue(root.right)
    largest = max(leftLargest, rightLargest, root.data)

    return largest

def countmaxValueThan(root, val):
    if not root:
        return 0

    leftvalue = countmaxValueThan(root.left, val)
    rightvalue = countmaxValueThan(root.right, val)

    if root.data > val:
        return 1 + leftvalue + rightvalue
    else:
        return leftvalue + rightvalue


x = takeInput()
printdetailedTree(x)

# count = countNumofNodes(x)
# print("count is",count)
#
# sum = sumofNodes(x)
# print("sum of all nodes is: ", sum)
#
# print("inorder is : ",end=" ")
# inorder(x)
# print()
# print("preorder is : ",end=" ")
# preorder(x)
# print()
# print("postorder is : ",end=" ")
# postorder(x)
#
# print( )
# largest = findmaxValue(x)
# print(largest)

val = 2
countmaxvalthan = countmaxValueThan(x,2)
print( f"Count of value greater than 2 ", countmaxvalthan)
#1 4 2 3 -1 -1 -1