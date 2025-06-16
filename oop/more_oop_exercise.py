class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    print(f"Person object for {self.name} created.")

  def __del__(self):
        print(f"Goodbye, {self.name}. The Person object is being deleted.")

# Example usage
p1 = Person("Alice", 30)

# Manually deleting the object to trigger the destructor
del p1


class Book:
   def __init__(self, title, author, pages):
      self.title = title
      self.author = author
      self.pages = pages

   def __str__(self):
      return f"You created a book titled {self.title} with {self.pages} pages, by {self.author}"
   
   def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

book = Book("Trial of Jimmy Johnson", "Sly Edagashe", 70)
print(repr(book))


class Animal:
   def __init__(self, name):
      self.name = name

   def eat(self):
      return f"{self.name} is eating"
   
   def sleep(self):
      return f"{self.name} is sleeping"
   

class Dog(Animal):
   def __init__(self, name, breed):
      self.breed = breed
      super().__init__(name)
    
   def bark(self):
      return f"{self.name} is barking"

   

goat = Animal("Goat")
print(goat.eat())
print(goat.sleep())

dog = Dog("Dog", "German Shepherd")
print(dog.bark())

## Single Inheritance
class Shape:
   def calculate_area(self):
      print("Area calculation not defined for generic shape.")

class Rectangle(Shape):
   def __init__(self, length, width):
      self.length = length
      self.width = width
      
   def calculate_area(self):
      self.answer = self.length * self.width
      return f"Area of Rectangle: {self.answer}"
   
rectangle = Rectangle(10, 6)
print(rectangle.calculate_area())

## Multiple Inheritance
class Bird:
   def fly(self):
      return "fly"

class Mammal:
   def run(self):
      return "run"

class Bat(Bird, Mammal):
   def __init__(self):
      super().__init__()

bat = Bat()
print(f"A bat is a bird and a mammal. A bat can {bat.fly()} and {bat.run()}")

## Polymorphism with Duck Typing
class Dog:
   def make_sound(self):
      print("Dog Woof")

class Cat:
   def make_sound(self):
      print("cat Meow")

class Bird:
   def make_sound(self):
      print("Bird Chirps")

def let_them_speak(animals):
   for animal in animals:
      animal.make_sound()


let_them_speak([Dog(), Cat(), Bird()])

## Class Methods for Counting Instances
class Book:
   total_books = 0 # Class variable to keep track of book instances
   def __init__(self, title, author):
      self.title = title
      self.author = author
      Book.total_books += 1
   
   @classmethod
   def display_total_books(cls):
      print(f"Total Books is: {cls.total_books}")
      

book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
Book.display_total_books()

## Static Method for Utility Calculation
class Calculator:
   @staticmethod
   def add(a, b):
      return a + b
   
   @staticmethod
   def multiply(a, b):
      return a * b
   
sum = Calculator().add(5, 7)
product = Calculator().multiply(6, 6)
print(f"The sum is: {sum} and the product is: {product}")

## Class Method for Factory Creation
class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age
      print('{}{}'.format(self.name, self.age))

   @classmethod
   def create_child(cls, name):
      return cls(name, 0)

# Example usage
child = Person.create_child("Tom")
print(f"Name: {child.name}, Age: {child.age}")

import json

def  process_json(data: dict, filename: str) -> dict:
   with open(filename, 'w') as file:
      json.dump(data, file)

   with open(filename, 'r') as file:
      data = json.load(file)

   return data
# Example
original_data = {"name": "Alice", "age": 30}
result = process_json(original_data, "person.json")
print(result)
