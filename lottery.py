from random import randrange

#This program will generate seven random digit lottery number from 0 to 9 
#and append to a list.


def main():
    numbers = []
    for n in range (0, 7):       
        x = (randrange(10))
        numbers.append(x)
    print(numbers)
main()








