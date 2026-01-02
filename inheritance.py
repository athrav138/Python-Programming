class Car:
  def get(name,n_seats):
    car_name = name
    number_of_seats = n_seats

class ToyotaCar(Car):
  
  def __init__(self,c):
    color = c

  def display():
    print(car_name)
    print(number_of_seats)
    print(color)

t1 = ToyotaCar("BLACK")
t1.get("TOYOTA FOrtuner",5)
t1.display()