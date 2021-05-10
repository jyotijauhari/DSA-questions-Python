class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self.__insert(value, self.root)

    def __insert(self, value, node):

        if not node:
            return Node(value)
        elif value < node.value:
            node.left = self.__insert(value, node.left)
        elif value > node.value:
            node.right = self.__insert(value, node.right)

        return node

    def inorder(self):
        self.__inorder(self.root)
        print()

    def __inorder(self, node):
        if not node:
            return

        self.__inorder(node.left)
        print(node.value, end=" ")
        self.__inorder(node.right)

    def delete(self, value):
        self.root = self.__delete(value, self.root)

    def __delete(self, value, node):
        if not node:
            return None

        if value < node.value:
            node.left = self.__delete(value, node.left)
        elif value > node.value:
            node.right = self.__delete(value, node.right)

            '''
                    5
                   / \
                      7
                      /\
                        9
                        \
                          10*
                            \
                            20
                              \
                               22 
                               
                    5
                   / \
                      7
                      /\
                        9
                        \
                          10
                            \
                            20*
                              \
                               22      
                               
                    5
                   / \
                      7
                      /\
                        9
                        \
                          10
                            \
                            20
                              \
                               22*
                               
                    5
                   / \
                      7
                      /\
                        9
                        \
                          10
                            \
                            20
                   
                   on 22 - none returned 
                   delete 22,          
                   replace 20 -> 22                                          
                               
                    5
                   / \
                      7
                      /\
                        9
                        \
                          10
                            \
                            22  
                            
                    replace 10 by 20
                    5
                   / \
                      7
                      /\
                        9
                        \
                          20
                            \
                            22  
                            
                Yeah done                                            
                                                                                        
            '''
        else:
            if (not node.left) and (not node.right):
                return None
            else:
                if node.left:
                    temp = node.left
                    while temp.right:
                        temp = temp.right
                else:
                    temp = node.right
                    while temp.left:
                        temp = temp.left

                replacementVal = temp.value
                self.__delete(replacementVal, self.root)
                node.value = replacementVal

        return node





    @classmethod
    def populate_from_list(cls, values):
        bst = BST()
        start = 0
        end = len(values) - 1
        bst.root = BST.__populate_from_list(values, start, end)

        return bst


    @classmethod
    def __populate_from_list(cls, values, start, end):

        if (start > end):
            return None

        midIdx = (start + end) // 2

        node = Node(values[midIdx])
        node.left = BST.__populate_from_list(values, start, midIdx-1)
        node.right = BST.__populate_from_list(values, midIdx+1, end)

        return node


bst = BST.populate_from_list([5, 7, 9, 10, 20, 22])
'''
        5
       / \
          7
          /\
            9
            \
              10
                \
                20
                  \
                   22 
'''
bst.inorder()

bst.delete(22)
bst.inorder()

bst.delete(9)
bst.inorder()