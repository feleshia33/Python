#Exercise #13: Population

start = int(input("Enter starting number of organisms: "))
percentage = int(input("Enter percentage number: "))
percent = percentage/100
days = int(input("Enter number of days: "))


print("Day Approximate\tPopulation")

for num in range(1, days +1):
    if num == 1:
        start = start
    elif days != 1:  
        start = (start * (1 + percent))
    print(num, "\t\t", format(start, '.2f'))
    
    
    



