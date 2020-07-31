#remove and rename function
import os

def main():
    #open file
    numbers = open("data.txt", "r")
    new_file = open("results.txt", "w")
    #read first line
    num = numbers.readline()
    print(num, end="")
    #set max and min
    max_num = num
    min_num = num
    #accumulator
    total = 0
    count = 0
    #loop thru num in file
    #calcuates total max min avg
    while num != "":
        total += int(num) 
        count += 1
        num = numbers.readline()
        print(num, end="")
        if  num > max_num:
            max_num = num
        if  min_num < num:
            min_num = min_num
    print("\nThe max number:", max_num, end="")
    print("\nThe min number:", min_num, end="")
    print("The total:", total, "\nThe avg:", total/count)
    #close file
    numbers.close()
    new_file.close()
    #delete original file
    os.remove("data.txt")
    #rename file
    os.rename("results.txt", "data.txt")
main()
