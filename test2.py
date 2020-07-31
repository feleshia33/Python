import random

#constant for max and min
MIN = 1
MAX = 100000

def main():
    #variable to control loop
    again = "y"    
    #roll rice
    while again == "y" or again == "Y":
        print("Roll\tPercentage")
        #store roll and %
        roll = (random.randint(MIN, MAX)) 
        roll_p = format((roll / MAX * 100), '.2f')
        #print roll and percentage
        print(roll, "\t", roll_p, "%")
        #another roll?
        again = input("Roll again? (y = yes) ")
main()
        
        
