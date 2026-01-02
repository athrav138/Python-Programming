class A:
  def __init__(self,a):
    self.a = a

  def display(self):
    print("The value a is: ",self.a)

class B(A):
  def __init__(self,b):
    super().__init__(b-2)
    self.b = b

  def display(self):
    super().display()
    print("The b is: ",self.b)

b1 = B(124)
b1.display()