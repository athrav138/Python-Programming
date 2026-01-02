class Student:
  def __init__(self,phy,chem,math):
    self.phy = phy
    self.chem = chem
    self.math = math

  @property
  def percentage(self):
    return (self.chem + self.phy + self.math)/3
  
s1 = Student(98,89,87)
print(s1.percentage)
s1.phy = 23
print(s1.phy)
print(s1.percentage)