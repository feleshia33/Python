#Budget Analysis: This program asks the user to enter the amount that he/she
#has budgeted for a month. A total of the monthly expense will total at the end
#and give and over/under budget depending on the amount spent.

budget = int(input("Enter your monthly budget amount: "))
num_expense = int(input("Enter the number of expenses for the month: "))
total = 0.0

for num in range(num_expense):
    number = int(input("Expense: "))
    total = total + number


print(total)
    
    
