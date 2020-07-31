#Exercise #10: Tuition Increase

#write a program with a loop that displays the projected semester tuition amount
#for the next 5 years

print()
print("Instruction: Write a program that reflects a 3% increase for the next 5")
print("years starting at tuition amount of $16,000. Tuition should result in")
print("per semester amount.")
print()

tuition = 8000 * 2  #8k per semester 
percentage = (1 + (3/100))
numOfYears = 5
start = 1   #starting year
print()
print("Year\tIncrease per semester")

for num in range(1, numOfYears +1):
    if tuition == tuition:
        tuition *= percentage
        semester = tuition / 2
        start = format(semester, '.2f') 
    print(num, "\t", start)
    
    

    
    
        
        

