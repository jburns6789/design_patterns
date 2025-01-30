class BankAccount:
    def __init__(self, account_number, balance):

        self._account_number = account_number # underscore makes protected

        self.__balance = balance # Private attribute double underscore
        # Have to use getters and setters on the object to get desired data

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Invalid balance")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount): #you want the logic to be done in the class so the logic remains encapsulated as well
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid with draw amount")

#Good practice to set preconditions and post conditions to ensure changes are vaild and correct before execution
#control how data is modified externally from the class

account = BankAccount("12345", 1000)

#accessing protected attribute (not recommeneded)
print("account number: ", account._account_number)

#accessing and modifing the private attribute through getter and setter methods
print("Initaial balance: ", account.get_balance())
account.set_balance(500)
print("Updated balnace:" , account.get_balance())

#using public methods that internally use the private attribute
account.deposit(100)
print("Balance after deposit: ", account.get_balance())
account.withdraw(50)
print("Balance after withdraw: ", account.get_balance())
        