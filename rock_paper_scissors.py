import random

# Display instructions
print("")
print("The rules of the game below:")
print("Paper beats rock, rock beats scissors, scissors beats paper.")
print("")

# Select player
print("Rock")
print("Paper")
print("Scissors")
print("")
player = input("Please select from the list: ").lower()
print("")

# Determine player
while True:
    if player == "1" or player == "Rock" or player == "rock":
        print("You have selected rock!")
        print("")
        break
    elif player == "2" or player == "Paper" or player == "paper":
        print("You have selected paper!")
        print("")
        break
    elif player == "3" or player == "Scissors" or player == "scissors":
        print("You have selected scissors!")
        print("")
        break
    else:
        player = input("That is an invalid choice, try again: ")
        print("")


# Computer choice
computer = ["Rock", "Paper", "Scissors"]
computer_choice = (random.choice(computer)).lower()

print("Computer has choosen: " + computer_choice + "!")
print("")

again = "Y"

# Determine winner

if computer_choice == player:
    print("It's a tie!")
elif computer_choice == "rock": 
    if player == "paper":
        print("You win!")
    else: 
        print("You lose") 
elif computer_choice == "scissors": 
    if player == "paper":
        print("You win!")
    else: 
        print("You lose") 
elif computer_choice == "paper": 
    if player == "paper":
        print("You win!")
    else: 
        print("You lose")   
else: 
    print("You lose!")
    again = input("Play again, enter 'Y' for yes or 'N' for no")





