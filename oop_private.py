class Student:
  name = "Atharv Milind Suryavanshi"

  def __init__(self,name):
    self.name = name

  def display(self):
    self.__show()
    print(self.name)

  def __show(self):
    print("Hello,")

s1 = Student("Atharv Milind Suryavanshi")
s1.display()
