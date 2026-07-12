#This program displays basic bank account information: name, account number, amount, and interest rate
#This program also allows for the interest rate to be adjusted
#And for withdrawing, depositing, and giving a balance
#interest can also be calculated based on the number of days.

#Creates account class
class BankAcct:

    #Defines basic and reused information
    def __init__(self, name, account_number, amount = 0.0, interest_rate = 0.0):
        self.name = name
        self.account_number = account_number
        self.amount = float(amount)
        self.interest_rate = float(interest_rate)

    #changes the initial interest rate into the new interest rate
    def adjust_interest_rate(self, new_rate):
        self.interest_rate = float(new_rate)

    #Allows the user to deposit money
    def deposit(self, amt):

        if amt > 0:
            self.amount += amt

        #If the user inputs an unreal number or a zero an error is displayed
        else:
            print("Deposit amount must be a positive number")

    #Allows the user to withdrawal money
    def withdraw(self,amt):
        if amt > 0:
            self.amount -= amt

        #The user cannot withdraw money they do not have
        elif amt > self.amount:
            print("insufficient funds")
        else:
            print("withdrawal amount must be a positive number")

    #Automatically calculates interest rate
    def calculate_interest(self, days):
        return f"{(self.interest_rate/100) * self.amount * (days/365)}"

    #Displays the basic information
    def __str__(self):
        return(f"Account Holder: {self.name}\n"
               f"Account Number: {self.account_number}\n"
               f"Balance: ${self.amount:,.2f}\n"
               f"Interest Rate: {self.interest_rate}"
               )

#Test function
def test_bank_account():
    #Defines the class inside the function with basic information
    account = BankAcct("Nathan Berenson", "ACCT1001", 1000.00, 5)

    print("Initial Account State: ")
    print(account)
    print()

    #Displays the new balance
    account.deposit(1000)
    print("New Balance")
    print(account)
    print()

    account.withdraw(200)
    print("New Balance")
    print(account)
    print()

    account.adjust_interest_rate(7)
    print("After adjusting interest rate to 7%:")
    print(account)
    print()

    #Simulates what the user will gain if their interest rate continued for x days
    interest = float(account.calculate_interest(10))
    #The ":2.f" rounds up to the nearest hundreds place
    print(f"Interest earned in {10} days: ${interest:.2f}")
    print()

    #Displays the final balance
    print()
    print("Final Balance: ")
    print(f"${account.amount}")

test_bank_account()

