def main():
    #input from user
    num = int(input("Select a number between 5 and 15: "))
    #validates integer
    while num < 5 or num > 15:
        print("The number entered is not between 5 and 15, try again.")
        num = int(input("Select a number between 5 and 15: "))
    #loop to print * and spaces
    for i in range(num):
        for j in range(num):
            #prints the num of * and spaces per input
            if(i == 0 or i == num -1 or j == 0 or j == num -1):
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()
main()        
