#Exercise 14: Compound Interest

#Get present value
present_value = float(input('Enter the present dollar amount: '))
#Get annual interest rate
rate = float(input('Enter the annual interest rate: '))
#Get compound value 
compound = float(input('Enter the compound rate annually or quarterly: '))
#Get number of years
years = float(input('Enter the number of years: '))
#Convert to decimal 
r = float((format(rate/100)))
#Compute compound times number of years 
comp_years = (years * compound)
#Calculation 
future_value = present_value * (1.0 + (r/compound)) **comp_years
#Show two decimal spaces and comma
future_amount = (format(future_value, '8,.2f'))
print('The future amount of the investment will be $',future_amount)


