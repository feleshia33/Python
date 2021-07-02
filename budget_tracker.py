#Budget Analysis: This program asks the user to enter the amount that he/she
#has budgeted for a month. A total of the monthly expense will total at the end
#and give and over/under budget depending on the amount spent.

budget = int(input("Enter your monthly budget amount: "))

while budget <= 0:
    print("Budget cannot be less that zero. Try again")
    budget = int(input("Enter your monthly budget amount: "))
    
num_expense = int(input("Enter the number of expenses for the month: "))
total = 0.0

for num in range(num_expense):
    print("Expense", num + 1, end="")
    number = int(input(": $ "))
    total += number
print("--")


print("Your total expenses for the month is $", format(total, ",.2f"),".", end="", sep="")

if total > budget:
    print(" You are over budget by ", format(total - budget, ",.2f"), ".", sep="")
else:
    print(" Congratulations! You are under budget by $", format(budget - total,",.2f"), ".", sep="")
    
    
