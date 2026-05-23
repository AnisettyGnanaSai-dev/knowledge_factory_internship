class Bank:
    def __init__(self, name, amount):
        self.name = name
        self.__amount = amount   
    
    def set_balance(self, amount):
        if amount >= 0:
            self.__amount = amount
        else:
            print("Invalid amount. Please enter a non-negative value.")

    def get_balance(self):
        return self.__amount
    
bank = Bank("My bank", 1000)

print(bank.get_balance())  # Output: 1000