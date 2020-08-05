NUM_EMP = 6


def main():
    hours = [0] * NUM_EMP

    for index in range(NUM_EMP):
        print("Enter the hours worked by employee ",
              index + 1, ": ", sep="", end="")
        hours[index] = float(input())

    pay_rate = float(input("Enter the hourly pay rate: "))

    for index in range(NUM_EMP):
        gross_pay = hours[index] * pay_rate
        print("Gross pay for employee ", index + 1, ': $',
              format(gross_pay, '.2f'), sep="")

main()
