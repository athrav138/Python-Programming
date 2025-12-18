x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

def add(a,b):
  return a+b

def subtract(a,b):
  return a-b

def multiply(a,b):
  return a*b

def division(a,b):
  return a/b

while True:
  operation = input("Enter operation name: (add,subtract,multiply,division):")
  if operation == 'add':
    print("Addition:",add(x,y))
  elif operation == 'subtract':
    print("Subtraction:",subtract(x,y))
  elif operation == 'multiply':
    print("Multiplication:",multiply(x,y))
  elif operation == 'division':
    print("Division:",division(x,y))
  else:
    print("Invalid operation.")
    break

