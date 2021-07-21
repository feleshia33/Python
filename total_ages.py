#This program calculates total ages

def main():
    #Get the user's age
    first_age = int(input("Enter your age: "))

    #Get the user's best friend's age
    seconf_age = int(input("Enter your friend's age: "))

    #Get the sum of both ages
    total = sum(first_age, second_age)

    #Display the total age
    print("Together you are", total, "years old.")

#The sum function accepts two numberic arguments and
# return te sum of those arguments.

def sum(num1, num2):
        result = num1 + num2
        return result

#Call the main function
main()
    
