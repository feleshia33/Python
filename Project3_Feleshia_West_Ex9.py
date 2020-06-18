#Exercise 9: Roulette Wheel Colors

pocket_number = int(input('Enter a pocket number: '))

if pocket_number == 0:
    print('The color is green!')
elif pocket_number <= 10 and pocket_number % 2 == 0:
    print('The color is black!')
elif pocket_number <= 10 and pocket_number % 2 != 0:
    print('The color is red!')
elif pocket_number <=18 and pocket_number % 2 == 0:
    print('The color is red!')
elif pocket_number <=18 and pocket_number % 2 != 0:
    print('The color is black!')
elif pocket_number <=28 and pocket_number % 2 == 0:
    print('The color is black!')
elif pocket_number <=28 and pocket_number % 2 != 0:
    print('The color is red!')
elif pocket_number <= 36 and pocket_number % 2 == 0:
    print('The color is red!')
elif pocket_number <= 36 and pocket_number % 2 != 0:
    print('The color is black!')
else:
    print('Error: Pocket number is not between 0 and 36')


