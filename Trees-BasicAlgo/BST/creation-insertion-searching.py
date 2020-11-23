#creation-insertion-traversal-searching.py

#BST aka Binary Search Trees

class Node:
  def __init__ (self,value):
    self.left = None
    self.right = None
    self.data = value

def insert(root, node):
  if root is None:
    root = node
    return

  if root.data < node.data:
    if root.right is None:
      root.right = node
    else:
      insert(root.right, node)  

  if root.data > node.data:
    if root.left is None:
      root.left = node
    else:
      insert(root.left, node)          

def preorder(node):
  if node is not None:
    print(node.data)
    preorder(node.left)
    preorder(node.right)


def inorder(node):
  if node is not None:
    preorder(node.left)
    print(node.data)
    preorder(node.right)

#search 
def search(root, key):
  if root is not None:
    if root.data == key:
      print("node found")
      return root

    if root.data < key :
      return search(root.right, key) 

    else :
      return search(root.left, key)     

root = Node(5)

insert(root, Node(3))

#	         5
#       /  	      \
#     3	            None

insert(root, Node(2))

#	         5
#       /  	      \
#     3	            None
#   /
#  2
insert(root, Node(4))

#	         5
#       /  	      \
#     3	            None
#   /   \
#  2     4
insert(root, Node(7))

#	         5
#       /  	      \
#     3	            7
#   /   \
#  2     4
insert(root, Node(6))

#	         5
#       /  	      \
#     3	            7
#   /   \        /
#  2     4      6
insert(root, Node(8))

#	         5
#       /  	      \
#     3	            7
#   /   \        /     \
#  2     4      6        8

# 5 3 2 4 7 6 8
preorder(root)

search(root, 8)
