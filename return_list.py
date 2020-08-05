#This program uses a function to create a list
#The function returns a reference to the list.

def main():
    #get a list with values sroted in it
    numbers = get_values()

    #display the values in the list
    print("The number in the list are: ")
    print(numbers)

    #the get_values function get a series of numbers
    #from the user ans store them in a list. The
    #function returns a reference to the list.
def get_values():
    #creates empty list
    values = []

    #create control variable
    again = 'y'

    #get values from the user and add them to
    #the list

    while again == 'y':
        #get a number and add it to the list
        num = int(input("Enter a number: "))
        values.append(num)

        #want to add another?
        print("Do you want to add another numbers?")
        again = input("y = yes, anything else = no: ")
        print()

    #return the list
    return values

main()
