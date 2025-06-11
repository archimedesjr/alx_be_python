# Student Class
class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def information(self):
    return f"{self.name} is {self.age} years old."

student1 = Student("Daniel", "20")
print(student1.information())

# Product Class
class Product:
  def __init__(self,  name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

  def total_value(self):
    return f"The total value of the products ordered by {self.name} is ${self.price * self.quantity}"
  
soap = Product("Temitayo", 500, 6)
print(soap.total_value())

# Handling ZeroDivisorError
try: 
  first_number = int(input("Enter your first number: "))
  second_number = int(input("Enter the second number: "))
  result = first_number/second_number
except ZeroDivisionError:
  print("Error: You cannot divide by zero")
else:
  print(result)

# Handling FileNotFoundError
try:
   f = open("text.txt")
except FileNotFoundError:
  print("File not Found")
else:
  f.read()
  f.close()


# Custom Exception
class  ValueTooHighError(Exception):
  def __init__(self, number):
    self.number = number

  def __str__(self):
    return f"Sorry, '{self.number}' is too high."
try:
  vak = int(input("Enter a number: "))
  if vak > 100:
    raise ValueTooHighError(vak)
  else: 
    print(f"{vak} is in the range of accepted numbers")
except TypeError:
  print("You entered a value that is not a number")
