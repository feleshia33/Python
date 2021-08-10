print("This program Ask the user for a number.")
print("Depending on whether the number is even or odd,")
print("and print out an appropriate message.")
print()

number = int(input("Enter a number from 1 to 1000: "))
even = number % 2

if even == 0:
    print(number, "is a even nnumber")
else:
    print(number, "is a odd nnumber")

print("================================")
print()
print("This program calcuates the length of a right triangle's hypotenuse.")

import math

def main():
    # Get the length of the triangle's two sides
    a = float(input("Enter the length of side A: "))
    b = float(input("Enter the length of side B: "))

    #Caculate the length of the hypotenuse
    c = math.hypot(a,b)

    # Display the length of the hypotenuse
    print("The length of the hypotenuse is", format(c, ",.2f"))

    #Call function
main()

    
