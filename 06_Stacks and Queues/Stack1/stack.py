class Stack:
    def __init__(self):
        self.__data = []

    def push(self, ele):
        self.__data.append(ele)

    def pop(self):
        if self.isEmpty() :
            print("Stack empty")
            return

        data = self.__data.pop()
        return data

    def top(self):
        if self.isEmpty():
            print("Stack empty")
            return

        data = self.__data[-1]
        return  data

    def size(self):
        return len(self.__data)

    def isEmpty(self):
        return self.size() == 0

s = Stack()

s.push(5)
s.push(6)

print(s.pop())

print(s.top())
