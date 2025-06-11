# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0  # Default attribute value

#     def get_descriptive_name(self):
#         full_name = f"{self.year} {self.make} {self.model}"
#         return full_name

#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")

#     def increment_odometer(self, miles):
#            self.odometer_reading += miles
class BankAccount():
  def __init__(self, account_balance):
    self.account_balance = account_balance
    self.initial_balance = 0

  def deposit(self, amount):
    self.amount = amount
    return self.account_balance + self.amount

  def withdraw(self, amount):
    self.amount = amount
    if self.account_balance > self.amount:
      return True
    else:
      return False
    
  def display_balance(self):
    return self.account_balance
