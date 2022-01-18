#Task3

def show_balance(balance):
    print("Your balance is",  balance)
    

def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    print("Your balance is ", balance+ amount)

def withdraw(balance):  
    amount = int(input("Enter amount to withdraw: "))
    print("Your withdrawal is " + balance - amount)

def logout(name):
    print("Goodbye " + name + "!")
    
