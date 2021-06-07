#This program gets a numeric test score from the
#user and displays the corresponding letter grade.

grade = int(input("Enter your test score: "))
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60


if grade >= A_SCORE:
    print("Your grade is an A.")
elif grade >= B_SCORE:
    print("Your grade is a B.")
elif grade >= C_SCORE:
    print("Your grade is a C.")
elif grade >= D_SCORE:
    print("Your grade is a D.")
else:
    print("Your grade is a F.")
