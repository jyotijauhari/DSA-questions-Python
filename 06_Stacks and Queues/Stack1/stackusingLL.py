class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def push(self, ele):
        newNode  = Node(ele)
        newNode.next = self.__head
        self.__head = newNode
        self.__count = self.__count + 1

    def pop(self):
        if self.isEmpty() is True:
            print("Stack is empty")

        data = self.__head.data
        self.__head = self.__head.next
        self.__count = self.__count - 1
        return  data

    def top(self):
        if self.isEmpty() is True:
            print("Stack is empty")
            return

        data = self.__head.data
        return data

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.size() == 0

    def printStack(self):
        dummyptr = self.__head
        len = self.__count
        for i in range(len):
            print(dummyptr.data, end= " ")
            dummyptr = dummyptr.next

s = Stack()
#01234
for i in range(5):
    s.push(i)

s.printStack()
print()

#  pop top 3 ele 4 3 2
for i in range(4):
    print(s.pop())

print("top is : ", s.top())

s.isEmpty()
s.size()

