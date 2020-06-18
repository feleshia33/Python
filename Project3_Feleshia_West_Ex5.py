#Exercise 5: Mass and Weight

mass = float(input('What is the mass of a coke of can? '))
weight = mass * 9.8

if weight > 500:
    print('The coke is too heavy.')
elif weight < 100:
    print('The coke is too light.')


