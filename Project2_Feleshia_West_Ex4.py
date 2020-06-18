#Exercise 4: Total Purchase

#Input prices
bread = float(input('Enter the amount for bread: ' ))
milk = float(input('Enter the amount for milk: '))
p_butter = float(input('Enter the amount for peanut butter: '))
jelly = float(input('Enter the amount of jelly: '))
spoons = float(input('Enter the amount for spoons: '))

#Computes sales tax
s_tax = float(7/100) + 1
s_tax_1 = float(7/100)

#Print subtotal
sub_total = float(bread + milk + p_butter + jelly + spoons)
st = format(sub_total, ',.2f')
print("The subtotal is $" ,st)

#Print sales tax
sales_tax = (sub_total * s_tax_1)
y = format(sales_tax, ',.2f')
print("The sales tax is $" ,y)

#Print total 
total = (sub_total * s_tax)
t = format(total, '5,.2f')
print("The total purchase is $"  ,t)
