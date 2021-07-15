# The following is used as a global constant
# the contribution rate.
CONTRIBUTION_RATE = 0.05

def main():
    gross_pay = float(input("Enter the gross pay: "))
    bonus = float(input("Enter the amount of bonuses:"))
    show_pay(gross_pay)
    show_bonus(bonus)

# The show_pay_contrib function accepts the gross pay
# as an agrument and displays the retirement
# contribution for hte total amount of pay.

def show_pay(gross):
    contrib = gross * CONTRIBUTION_RATE
    print("Contribution for gross pay: $", format(contrib, ".2f"), sep="")


def show_bonus(bonus):
    print("Contribution for bonuses: $", format(contrib, ".2f"), sep="")


main()
