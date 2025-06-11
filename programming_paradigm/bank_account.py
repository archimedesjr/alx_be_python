class BankAccount:
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
    return f"Current Balance: $[{self.account_balance}]"