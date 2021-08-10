# This program calculates the total monthly and annual cost from the user

# Gets monthly automobile cost from user
loan_payment = float(input("Enter monthly car payment: "))
insurance = float(input("Enter monthly car insurance: "))
gas = float(input("Enter monthly car gas usage amount: "))
oil = float(input("Enter monthly car oil change amount: "))
tires = float(input("Enter monthly car tire amount: "))
maintenance = float(input("Enter monthly car maintenance amount: "))
total_monthly = loan_payment + insurance + gas + oil + tires + maintenance
total_yearly = (loan_payment + insurance + gas + oil + tires + maintenance) * 12

print("=================================================")
print("Your total monthly expenses is $: ", total_monthly)
print("Your total yearly expenses is $: ", total_yearly)
