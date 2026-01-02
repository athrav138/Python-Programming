# Changing the value of class variable

class Num:
    a = 10

    def __init__(self, b):
        Num.a = b

    def display(self):
        print(Num.a)
        
"""
    @classmethod
    def __init(cls,b):
    cls.a = b
"""

p1 = Num(12)
p1.display()
print(Num.a)
