from abc import ABC, abstractmethod
class BankAccount (ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass
    @abstractmethod

    def check_balance(self):
        pass
class savingsAccount(BankAccount):
        def __init__(self, balance):
            self.balance += balance

        def deposit(self, amount):
            self.balance += amount
            return True
        else:
            return False

        def 