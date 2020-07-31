#Exercise #8: Sum of Numbers


#get input from user
print("Enter a positive number. Enter a negative number to end.")
number = float(input("Enter a positive number: "))

#accumulator variable 
sum_num = 0.0

#determine if number is positive if so add to total
if number > 0:
    sum_num += number

#get series of numbers and only adds positive number
while number > 0:
    number = float(input("Enter a positive number: "))
    if number > 0:
        sum_num +=number
        
#prints sum of positive numbers        
print("Sum of positive numbers: ", sum_num)
    
