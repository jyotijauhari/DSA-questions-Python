# l = [5,6,7,8]
# front = 1
# n = [None]*2*len(l)
# print(n)
# for i in range(len(l)):
#    n[i] = l[(front + i)%len(l)]
#    front = 0
#
#
# print(n)

class CircularQueue:

    def __init__(self):
        self.__data = [None] * 10
        self.__front = 0
        self.__end = -1
        self.__size = 0

    def insert(self, value):

        if self.__size == len(self.__data):
            old = self.__data
            self.__data = [None] * (2*len(old))
            for i in range(len(old)):
                self.__data[i] = old[(self.__front + i) % len(old)]
                self.__front = 0
                self.__end = len(old) - 1

        self.__end = (1 + self.__end) % len(self.__data)
        self.__data[self.__end] = value
        self.__size += 1

    def delete(self):
        if self.__size == 0:
            return None

        value = self.__data[self.__front]
        self.__front = (self.__front + 1) % len(self.__data)
        self.__size -= 1
        return value

    def front(self):
        return self.__data[self.__front]

    def size(self):
        return self.__size

    def display(self):
        for i in range(self.__size):
            print(self.__data[(self.__front + i) % len(self.__data)], end=" ")
        print()


queue = CircularQueue()

print("Insering 0 to 9: ")
for i in range(10):
    queue.insert(i)

queue.display()
print()

print("Deleting 5 values")
for i in range(5):
    queue.delete()

queue.display()
print()

for i in range(11,20):
    queue.insert(i)
    print("inserting",+ i)
    queue.display()


