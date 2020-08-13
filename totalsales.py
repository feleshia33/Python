#This program asks the user to enter a store's sales for each day of the week.
#The amounts should be stored in a list. Using a loop to calculate the total
#sales for the week and display the result.

def main():
    #empty list to hold daily amounts
    day = []
    total = 0

    new_day = "y"
    #loop thru sales for the week
    while new_day == "y":
        workday = float(input("Enter the sales amount starting with Sunday: "))
        #appends day's sale into a list
        day.append(workday)
        #new day's amount?
        new_day = input("Enter a new day? y = yes and n = no ")
    #print sales for each day
    print("Total sales: ")
    #loops thru days and gets total
    for workday in day:
        #add each days total
        total +=workday
    print(total)

main()

        


    
