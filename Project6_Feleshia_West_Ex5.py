#Exercise 5: Sum of Numbers

def main():
    #open file
    numbers = open("numbers.txt", "r")
    #accumlator
    sum = 0
    #loop through numberss
    for num in numbers:
        total = int(num)
        sum += total
    #close file
    numbers.close()    
    #print total
    print("The sum of all the numbers is", sum)    
    
main()
