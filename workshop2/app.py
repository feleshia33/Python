from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

print("        === Automated Teller Machine ===          ")

#Recv' users name/pin
name = input("Enter a name to register: ").lower()
pin = input("Enter pin: ")
balance = float(0)
print(name, " has been registered with a starting balance of " + "$", balance, ".")

print("LOGIN")

#Validates user input
print("        === Automated Teller Machine ===          ")
while True:
    name_to_validate  = input("Enter your user name: ").lower()
    pin_to_validate = input("Enter your pin number: ")
    
    if pin == pin_to_validate and name == name_to_validate:
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")
        print("        === Automated Teller Machine ===          ")
        
#Display options        
while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance) 
    elif option == "2":
        account.deposit(balance)
        # return balance
        account.show_balance(balance)
    elif option == "3":
        account.withdraw(balance)
        # return balance
        print(balance)
        account.show_balance(balance)  
    elif option == "4":
        account.logout(name)
        break

 