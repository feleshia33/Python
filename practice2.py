# This program Ask the user for a number.
# Depending on whether the number is even or odd,
# print out an appropriate message.

number = int(input("Enter a number from 1 to 100: "))
even = number % 2

if even == 0:
    print(number, "is a even nnumber")
else:
    print(number, "is a odd nnumber")
