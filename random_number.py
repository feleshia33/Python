#This program displays a random number in the range of 1 through 10.

import random

def main():
    #Get a random number
    number = random.randint(1,10)
    #Display the number
    print("The random number is ", number)

#Call function
main()


def main1():
    print("The five random numbers are: ")
    for count in range(5):
        #Get random number
        number1 = random.randint(1, 100)
        #Display the number
        print(number1)

#Call function
main1()
