#This program is a 5 question quiz and answer.

print("Welcome to the 5 question quiz!")
play = input("Would you like to play? Type yes or no. ").lower()
counter = 0

if play != "yes":
    print("Maybe next time.")
    quit()

print("Let's begin.")

#Q1
answer = input("Question 1: What is the capital of Texas? ").lower()
if answer == "austin":
    print("correct!")
    counter +=1
    print()
    
else:
    print("sorry, that is not correct.")
    print()
    
#Q2
answer = input("Question 2: What is hola is English? ").lower()
if answer == "hello":
    print("correct!")
    counter +=1
    print()
else:
    print("sorry, that is not correct.")
    print()
#Q3
answer = input("Question 3: What color is the grass? ").lower()
if answer == "green":
    print("correct!")
    counter +=1
    print()
else:
    print("sorry, that is not correct.")
    print()
    
#Q4
answer = input("Question 4: What has wings and can fly in the air? ").lower()
if answer == "birds" or "birds":
    print("correct!")
    counter +=1
    print()
else:
    print("sorry, that is not correct.")
    print()
    
#Q5
answer = input("Question 4: Complete the sentence. Happy Birthday to you, Happy _____"
               "to you? ").lower()
if answer == "birthday":
    print("correct!")
    counter +=1
    print()
else:
    print("sorry, that is not correct.")
    print()
    

print("Your total score is:", counter, "out of 5.")
