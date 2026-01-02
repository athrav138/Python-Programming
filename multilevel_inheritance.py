class Car:
  def get(self,name,n_seats):
    self.car_name = name
    self.number_of_seats = n_seats

class ToyotaCar(Car):
  
  def __init__(self,c):
    self.color = c

class Fortuner(ToyotaCar):
  
  def display(self):
    print(self.car_name)
    print(self.number_of_seats)
    print(self.color)


t1 = Fortuner("BLACK")
t1.get("TOYOTA FOrtuner",5)
t1.display()