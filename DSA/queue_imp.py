class QueueLine:
  def __init__(self):
    self.q = []
    

  def enqueue(self, x):
    self.q.append(x) 

  def dequeue(self):
    self.q.pop(0)  

  def front(self):
    return self.q[0]  

  def printq(self):
    for i in self.q:
      print(i, end = " ")
    print()  
    
q1 = QueueLine()     
q1.enqueue(5)
q1.enqueue(6)
q1.enqueue(7)
q1.enqueue(8)
q1.enqueue(9)
q1.printq()

q1.dequeue()
q1.printq()

q1.front()


