#This program calculates sales commissions.

keep_going = "y"

while keep_going == "y":
    sales = float(input("Enter the amout of sales: "))
    comm_rate = float(input("Enter the commision rate: "))
    
    commission = sales * comm_rate

    print("The commissionis $", format(commission, ",.12"), sep="")

    keep_going = input("Do you want to calculate another " +"commission (Enter y for yes): ")
