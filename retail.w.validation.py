# This program calculates retail prices.

MARK_UP = 4.0
another = 'y'

#Process one or more items.
while another == 'y' or another == "Y":
    #Get the item's wholesales cost.
    wholesale = float(input("Enter the item's " + "wholesale cost: "))

    #Validate the wholesale cost.
    while wholesale < 0:
        print("Error: the cost cannot be negative.")
        wholesale = float(input("Enter the correct" + "wholesale cost: "))


    #Calculate the retail price.
    retail = wholesale * MARK_UP

    #Display the retail price.
    print("Retail price: $", format(retail, ',.2f'), sep="")

    #Do this again?
    another = input("Do you have another item? " +
                    "(Enter 'y' for yes OR 'n' for no): ")
