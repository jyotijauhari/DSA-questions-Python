#(insert - enqueue, delete - dequeue)
# inserting or deleting an element at the beginning requires shifting all of the other elements by one, requiring O(n) time.

# insertion efficient queue (prob - removal take O(n) time and to removal n item n2 time

class Customqueue():
    def __init__(self):
        self.__data = list()

    def insert(self, ele):
        self.__data.append(ele)

    def delete(self):
        return self.__data.pop(0)

    def printq(self):
        for i in self.__data:
            print(i, end=" ")

    def front(self):
        return  self.__data[0]

    def size(self):
        return len(self.__data)



#removal efficient queue - insertion take O(n) time , and to insert n item n2 time

class Customqueue():
    def __init__(self):
        self.__data = list()

    def insert(self, ele):
        self.__data.append(0,ele)

    def delete(self):
        return self.__data.pop()

    def printq(self):
        for i in self.__data:
            print(i, end=" ")

    def front(self):
        return self.__data[0]

    def size(self):
        return len(self.__data)