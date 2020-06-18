#This program calcuates the sum of a series
# of numbers entered by the user.

MAX = 5 #The max number

#Initialize an accumulor variable
total = 0.0

#Explain what we are doing.
print('This program cacluates the sum of')
print(MAX, 'numbers you will enter.')

#Get the numbers and accmulate them.
for counter in range(MAX):
    number = int(input('Enter a number: '))
    total = total + number

#Display the total of the numbers.
print('The total is', total)
