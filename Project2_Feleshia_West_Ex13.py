#Exercise 13: Planting Grapevines

#Get input
numFeet = float(input("How many feet is each row? "))
end_post = float(input("What is the amount of space used by the end-post assembly? "))
space = float(input("How much space is in betwen each of the vines? "))

#Calculation with two decimal points
v = ((numFeet - (2 * end_post)) / space)
total = format(v, ',.2f')

#Output
print("The number of grapevines that will fit in each row is", total)

