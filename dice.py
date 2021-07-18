#This program the rolling of dice

import random

#Constants for the min and max rand nums

MIN = 1
MAX = 6

def main():
    #Create a variable to control the loop
    again = "y"

    #Simulate rolling of the dice
    while again == "y" or again =="Y":
        print("Rolling the dice...")
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

        # Do another roll of the dice?
        again = input("Roll them again?? (y = yes): ")
        
#Call function
main()
