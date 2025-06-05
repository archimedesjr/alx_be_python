from random import randint, choice
# Greet Function
def greet(name):
  print(f"Hello, {name}")
greet("Temitayo")

# Area of Rectangle
def area(length, width):
  print(length * width)
area(2, 3)

#Odd or Even number
def check_number(number):
  if number % 2 == 0:
    print("You entered an even number")
  else:
    print("You entered a odd number")
check_number(54)

# List Exercise
favorite_fruit = ["Apple", "Banana", "Orange", "Pear", "Grape"]
print(favorite_fruit[1])

#Dictionary Exercise
my_fav_book = {
  "title" : "Broken",
  "author" : "Fatima Bala",
  "genre" : "Romance"
}
genre = my_fav_book.get("genre")
print(genre)

#Set Exercise
random_numbers = {randint(1,10) for _ in range(20)}
print(random_numbers)

# Local and Global Scope Instruction
x = "global x"
def my_function():
  x  = "inner x"
  print(x)
my_function()
print(x)

# Namespace Exploration
def counting_function():
  count = 5
  def logging_function():
    count = 10
    print(count)
  
  logging_function()
  print(count)
counting_function()

#  Scope Hierarchy Instructions
# Global Scope
x = "I'm global"

def outer():
    # Enclosing Scope
    x = "I'm in the enclosing scope"

    def inner():
        # Local Scope (No x defined here, so Python will look in enclosing, then global)
        print("Accessing x in LEGB order:")
        print("Enclosing x:", x)  # Will print the enclosing x

        # To access the global x, use the globals() function
        print("Global x:", globals()['x'])

    inner()

outer()

