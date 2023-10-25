class BankAccount:
  def __init__(self, account_number, account_holder_name):
      self.__account_number = account_number
      self.__account_holder_name = account_holder_name
      self.__account_balance = 0

  def deposit(self, amount):
      if amount > 0:
          self.__account_balance += amount
          return f"Deposited {amount} dollars. New balance: {self.__account_balance}"
      else:
          return "Invalid deposit amount."

  def withdraw(self, amount):
      if 0 < amount <= self.__account_balance:
          self.__account_balance -= amount
          return f"Withdrew {amount} dollars. New balance: {self.__account_balance}"
      else:
          return "Invalid withdrawal amount."

  def display_balance(self):
      return f"Account balance for {self.__account_holder_name} (Account #{self.__account_number}): {self.__account_balance}"

# Test the BankAccount class
account = BankAccount(123456, "John Doe")
print(account.deposit(1000))
print(account.withdraw(500))
print(account.display_balance())
