#This program will guess the magic number

from random import randrange

#rand_num = (randrange(6))
rand_num = 5
guess = int(input("Guess the random number between1 to 5: "))


while guess !=rand_num:
    print("Sorry that is not the random number, guess again.")
    guess = int(input("Guess the random number between 1 to 5: "))
    
else:
        print("Yea! You've guess the random number of ", rand_num,"!", sep="")

        
