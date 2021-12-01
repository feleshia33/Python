import random

# Display instructions
print("")
print("The rules of the game is below:")
print("Paper beats rock, rock beats scissors, scissors beat paper.")
print("")

# Select player
print("1) Rock")
print("2) Paper")
print("3) Scissors")
player = input("Please select a player from list: ")
print("")

# Determine player
while True:
    if player == "1" or player == "Rock" or player == "rock":
        print("You have selected Rock!")
        print("")
        break
    elif player == "2" or player == "Paper" or player == "paper":
        print("You have selected Paper!")
        print("")
        break
    elif player == "3" or player == "Scissors" or player == "scissors":
        print("You have selected Scissors!")
        print("")
        break
    else:
        player = input("That is not a valid player, try again: ")
        print("")

computer = ["Rock", "Paper", "Scissors"]
computer_choice = (random.choice(computer))

print("Computer chose:", computer_choice)








