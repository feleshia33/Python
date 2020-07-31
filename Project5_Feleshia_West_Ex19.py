#Exercise #19: Future Value


#input from users
def main():
    #Get present value
    present_value = float(input('Enter the present dollar amount: '))
    #Get monthly interest rate
    rate = float(input('Enter the monthly interest rate: '))
    #convert % to a decimal
    int_rate = (rate/100)
    #Get months in account
    months = float(input('Enter the number of months the money will be in account: '))
    future(present_value, int_rate, months)
def future(p, r, m):
    #Calculation 
    future_value = (p * (1 + r)**m)
    print("The future amount will be ", format(future_value, '.2f'))



main()
