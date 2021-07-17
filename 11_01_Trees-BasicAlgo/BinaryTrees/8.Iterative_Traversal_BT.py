# class Node:
#     def __init__(self, k):
#         self.left = None
#         self.right = None
#         self.key = k


# def itrInorder(root):
#     if root is None:
#         return

#     st = []
#     curr = root
#     while curr is not None:
#         st.append(curr)
#         curr = curr.left

#     while len(st) > 0:
#         curr = st.pop()
#         print(curr.key)
#         curr = curr.right

#         while curr is not None:
#             st.append(curr)
#             curr = curr.left


# # Driver Code

# root = Node(100)
# root.left = Node(200)
# root.right = Node(300)
# root.left.left = Node(400)
# root.left.right = Node(500)

# itrInorder(root)

class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.key = k


def itrPreorder(root):
    if root is None:
        return

    st = [root]

    while len(st) > 0:
        curr = st.pop()
        print(curr.key)

        if curr.right is not None:
            st.append(curr.right)

        if curr.left is not None:
            st.append(curr.left)


# Driver Code

root = Node(100)
root.left = Node(200)
root.right = Node(300)
root.left.left = Node(400)
root.left.right = Node(500)
root.right.right = Node(600)

itrPreorder(root)

