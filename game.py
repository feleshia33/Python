# This program will write a quiz for the user to be scored on.

question = print("What is the capitol of Texas? ")
answer = input("a. Orlando, b. Austin, c. Marfa, d. Ernest ") 
            

while answer != "Austin" or "austin" or "b":
    print("That is the not the correct answer, try again.")
    answer = "Austin" or "austin"
    question = print(input("What is the capitol of Texas? "))
   
    
