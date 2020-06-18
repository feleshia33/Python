#Exercise #3: Budget Analysis

#get input from user
budget = float(input('Enter your budget for the month: '))
expenses = int(input('How many expense account do you have? '))

#set total to 0
total = 0.0

#total each expense
for counter in range(expenses):
    number = int(input('Enter an expenses: '))
    total = total + number


print('Your total expenses are', total)

if budget > total:
    print('You are under budget by', budget - total)
else:
    print('You are over budget by', total - budget)
