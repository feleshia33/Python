#Exercise 11: Male and Female Percentages

#Get num of fe/males 
numOfFemales = int(input('Enter the number of females:  '))
numOfMales = int(input('Enter the number of males: '))

#Calculate total
total = numOfFemales + numOfMales

#Output % of fe/males registered & round two decimal places
print("The number of females registered is ", format((numOfFemales /total), '.0%'))
print("The number of males registered is ", format((numOfMales /total), '.0%'))














