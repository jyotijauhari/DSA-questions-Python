#push(), pop(), isEmpty() and top() all take O(1) time.

class CustomStack:
    def __init__(self):
        self.__data = list() #local var

    def push(self, ele):
        self.__data.append(ele)

    def pop(self):
        if self.__data:
            return  self.__data.pop()
        else:
            print("empty")


    def top(self):
        return self.__data[-1]

    def size(self):
        return len(self.__data)

    def printstack(self):
        for i in self.__data:
            print(i, end=" ")
        print()

stack = CustomStack()
stack.push(5)
stack.push(6)
stack.push(6)
stack.push(7)
stack.push(8)
stack.printstack()
stack.pop()
stack.printstack()
print(stack.top())
stack.pop()
stack.printstack()
stack.pop()
stack.printstack()
stack.pop()
stack.printstack()
stack.pop()
stack.printstack()
stack.pop()
stack.printstack()

