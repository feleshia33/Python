#Exercise #12: Calculating the Factorial of a Number

num = int(input("Enter a nonnegative integer: "))
fac = 1

for i in range(1, num + 1):
    fac = fac * i

print("The factorial of", num, "is", format(fac, ',.0f'))


