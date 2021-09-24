#Creation and traversal Binary Trees
#Binary Tree 

#creation
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

#traversal inorder
def inorder(node):
    if(node is not None):
        inorder(node.left)
        print(node.data)
        inorder(node.right)

#traversal pre-order
def preorder(node):
  if(node is not None):
    print(node.data)
    preorder(node.left)
    preorder(node.right)

#traversal post-order
def postorder(node):
  if(node is not None):
    postorder(node.left)
    postorder(node.right)
    print(node.data)

# create root
root = Node(4)

#	    4
#	  /   \
#	None  None


root.left = Node(5)
root.right = Node(6)

# 5 becomes left child and 6 become right child of 1
#		           4
#		       /       \
#		      5	        6
#	      /  \      /   \
#     None None  None  None


root.left.left = Node(7)


# 7 becomes left child of 5
#		           4
#		       /       \
#		      5	        6
#	      /  \      /   \
#      7   None  None  None
#     / \
#  None  None

#inorder(root)
preorder(root)
