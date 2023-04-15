vanifrom abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def display_account_type(self):
        pass

    @abstractmethod
    def display_account_details(self):
        pass

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}")
        print(f"New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}")
            print(f"New balance: ${self.balance}")
        else:
            print("Insufficient balance")

class CheckingAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def display_account_type(self):
        return "Checking Account"

    def display_account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.display_account_type()}")
        print(f"Balance: ${self.balance}")

class SavingAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def display_account_type(self):
        return "Saving Account"

    def display_account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.display_account_type()}")
        print(f"Balance: ${self.balance}")

class BusinessAccount(Account):
    def __init__(self, account_number, balance, company_name):
        super().__init__(account_number, balance)
        self.company_name = company_name

    def display_account_type(self):
        return "Business Account"

    def display_account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.display_account_type()}")
        print(f"Company Name: {self.company_name}")
        print(f"Balance: ${self.balance}")
