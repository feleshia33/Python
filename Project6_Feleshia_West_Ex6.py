#Exercise 5: Average of numbers

def main():
    #open file
    numbers = open("numbers.txt", "r")
    #accumlator
    count = 0
    #accumlator
    total = 0
    for nums in numbers:
        sum = int(nums)
        count += 1
        total += sum
    #close file
    numbers.close()
    #print avg
    avg = int(total / count)
    print("The average of all the numbers is", avg)
main()

