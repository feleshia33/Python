# The following is used as a global constant
# the contribution rate.


CONTRIBUTION_RATE = 0.05

def main():
    gross_pay = float(input("Enter the gross pay: "))
    bonus = float(input("Enter the amount of bonuses:"))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)

