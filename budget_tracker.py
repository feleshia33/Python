#Budget Analysis: This program asks the user to enter the amount that he/she
#has budgeted for a month. A total of the monthly expense will total at the end
#and give and over/under budget depending on the amount spent.

budget = int(input("Enter your monthly budget amount: "))
num_expense = int(input("Enter the number of expenses for the month: "))
total = 0.0

for num in range(num_expense):
    print("Expense", num + 1, end="")
    number = int(input(":$"))
    total = total + number


print("Your total expenses for the month is", format(total, ",.2f"),".", end="")

if total > budget:
    print("You are over budget by", format(total - budget, ",.2f"), ".")
else:
    print("You are under budget by", format(budget - total,",.2f"), ".")
    
    
