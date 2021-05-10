class CircularQueue:
    def __init__(self):
        self.__data = list()
        self.__front = 0
        self.__end = -1
        self.__size = 0

    def insert(self, ele):
        if self.__size == len(self.__data):
            old = self.__data
            self.__data = 2*(len(old))
            for i in range(len(old)+1):
                self.__data[i] = old[(self.__front+i)%len(old)] #**
                self.__front = 0
                self.__end = len(old) - 1

        self.__end = ( self.__end +1 ) % len(self.__data)
        self.__data[self.__end] = ele
        self.__size += 1

    def delete(self):
        if self.__size == 0:
            return None
        value = self.__data[self.__front]
        self.__front = (self.__front + 1)%len(self.__data)
        self.__size -= 1
        return value

queue = CircularQueue()
queue.insert()

