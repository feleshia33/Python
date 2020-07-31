def main():
     #(1)open file
     in_file = open('steps.txt', 'r')
     #read num steps adds month and num of days
     ave(in_file, 'January', 31)
     ave(in_file, 'February', 28)
     ave(in_file, 'March', 31)
     ave(in_file, 'April', 30)
     ave(in_file, 'May', 31)
     ave(in_file, 'June', 30)
     ave(in_file, 'July', 31)
     ave(in_file, 'August', 31)
     ave(in_file, 'September', 30)
     ave(in_file, 'October', 31)
     ave(in_file, 'November', 30)
     ave(in_file, 'December', 31)
     #(2) close file
     in_file.close()
#ave func with arguments and calculates avg monthly steps     
def ave(file, month, days):
     #(3)accumulator
     total = 0
     for day in range(days):
         #total amount per day per month 
         total += int(file.readline())
     #(4) average per month
     average = total / days
     print('Average steps taken in', month, "is", format(average, ',.0f'))
#(5)call func     
main()
    
    
