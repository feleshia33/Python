import random
def main():
    #creates user name
    username()
    #creates password
    password()
    #creates pin
    pin()
    #gets email and prints message for user
    email()
def username():
    #get first name from user
    firstname = input("Enter your first name: " )
    #converts to uppercase
    u = firstname.upper()
    #creates random number btw 1 - 1000
    rnum = random.randint(1, 1000)
    #print user name and generates a random num to end
    print("Your username will be: ", u, end="")
    print(rnum)
    print("\n~~~~~~ Next ~~~~~~")
def password():
    #instructions
    print("Password critera must contain letters or numbers")
    print("AND a least one special characters")
    #get password from uswer
    password = input("Enter a password: " )
    #validates password to include any special character
    while password.isalnum() == True:
        print("Password critera not met, try again")
        password = input("Enter a password: " )
    else:
        #strips any white spaces before and after password
        print("Your password is", password.strip())
    print()
    print("~~~~~~ Next ~~~~~~")  
def pin():
    #instructions
    print("Pin must have only numbers")
    print("Create a backup pin")
    #pin input from user
    pin = input("Create a pin number: ")
    #determine if pin number contains only numbers 
    while pin.isdigit() == False:
        print("Pin number must only have numbers, try again")
        pin = input("Create a pin number: ")
    #validates pin number to be digits only
    if pin.isdigit():
        print("Pin number accepted")
    else:
        print("Pin number must only contain numbers")
    print()
    print("~~~~~~ Next ~~~~~~")
def email():
    #gets users gmail address
    email = input("Enter your gmail address: ")
    #determins whether email ends with "gmail.com"
    while email.endswith("gmail.com") == False:
        print("Please enter a valid gmail account")
        email = input("Enter your gmail address: ")
    else:
        #converts gmail address to lower case
        print("Check your gmail at", email.lower(), "for additional information")
    print()
    #replaces Next with End
    stop = "Next"
    end = stop.replace("Next", "End")
    print("~~~~~~",end,"~~~~~~")
main()




    
