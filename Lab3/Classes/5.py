class BankAccount:
    pass
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} accepted. New balance: {self.balance}")
        else:
            print(f"Invalid deposit amount. Please enter a positive value")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of {amount} accepted. New balance: {self.balance}")
            else:
                print("Insufficient amount. No withdrawal allowed")
        else:
            print("Invalid withdrawal amount. Please enter a positive value")

account = BankAccount("Nikita", 0)

account.deposit(1000)
account.withdraw(500)
account.withdraw(500)
account.withdraw(500)
account.deposit(1000)
