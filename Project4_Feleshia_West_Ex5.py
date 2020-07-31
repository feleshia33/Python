#Exercise #5: Average Rainfall

#number of years of rainfall
years = int(input("How many years of rainfall? "))
#number of months per year
months = 12

#determine avg rainfall each year
for year in range(years):
    #accumlator
    total = 0.0
    #get rainfall for each year
    print("Year:", year + 1)
    print("------")
    for month in range(months):
        print("Rainfall month", month + 1, end='')
        m_inches = float(input(': '))
        #add score
        total += m_inches
       


    #caclulate avg inches per year
    average = (total / months)
    print("-------------------")
    print("Total months: ", months)
    print("Total inches: ", format(total, '.2f'))
    print("Average inches per month for the year is: ", format(average, '.2f'))
    print("-------------------")
    



    
            
        
