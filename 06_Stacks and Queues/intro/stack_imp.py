class Stack:
  def __init__(self):
    self.s = []
    

  def push(self, x):
    self.s.append(x) 

  def pop(self):
    self.s.pop()  

  def top(self):
    return self.s[-1]  

  def prints(self):
    for i in self.s:
      print(i, end = " ")
    print()  
    
s1 = Stack()     
s1.push(5)
s1.push(6)
s1.push(7)
s1.push(8)
s1.push(9)
s1.prints()

s1.pop()
s1.prints()

s1.top()

