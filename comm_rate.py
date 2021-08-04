# This program calculates a salesperson's pay at
# Make Your Own Music

def main():
    #Get the amount of sales.
    sales = get_sales()

    #Get the amount of advancedd pay.
    advanced_pay = get_advanced_pay()

    #Determine the commission rate.
    comm_rate = determine_comm_rate(sales)

    #Calculate the pay.
    pay = sales * comm_rate - advanced_pay

    #Display the amount of pay.
    print("The pay is $', format(pay, ',.2f')", sep=" ")

    #Determine whether the pay is negative
    if pay < 0:
        print("The Salesperson must reimburse the company.")
        
