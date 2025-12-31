class Student :
  def __init__(self,name,m1,m2,m3):
    self.name = name
    self.m1 = m1
    self.m2 = m2
    
    self.m3 = m3

  @staticmethod
  def greet(name):
    print("Hello,",name)

  def display(self):
    print(f"The information of student {self.name} is :")
    print(f"The average of marks is: ",(self.m1 + self.m2 + self.m3)/3)

s1 = Student("Atharv",99,99,99)
s1.greet(s1.name)
s1.display()
  
  