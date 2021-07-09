#This program is a 5 question quiz and answer.

print("Welcome to the 5 question quiz!")
play = input("Would you like to play? Type 'y' for Yes or 'n' for No. ")

if play != "y" or "Y":
    #quit()
    
    print("Let's begin.")

answer = input("Question 1: What is the capital of Texas? ").lower()
if answer == "austin":
    print("correct!")
else:
    print("sorry, that is not correct.")

answer = input("Question 2: What is hola is English? ").lower()
if answer == "hello":
    print("correct!")
else:
    print("sorry, that is not correct.")

answer = input("Question 3: What color is the grass? ").lower()
if answer == "green":
    print("correct!")
else:
    print("sorry, that is not correct.")

answer = input("Question 4: What has wings and can fly in the air? ").lower()
if answer == "birds" or "birds":
    print("correct!")
else:
    print("sorry, that is not correct.")

answer = input("Question 4: Complete the sentence. Happy Birthday to you, Happy _____"
               "to you? ").lower()
if answer == "birthday":
    print("correct!")
else:
    print("sorry, that is not correct.")
