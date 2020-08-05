import random

while True:
    player = input("rock, paper, scissors? : ")
    computer = random.choice(['rock', 'paper', 'scissors'])

    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "rock":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", computer, "smashes", computer)
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("Check your spelling!")
