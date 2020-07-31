#Exercise #18: Prime Number List

def is_prime():    
    num = 1
    #start at 2 loop thru 100
    while(num <= 100):
        count = 0
        i = 2
        while(i <= num//2):
            if(num % i == 0):
                #count prime num
                count = count + 1
                break
            i = i + 1
        if (count == 0 and num != 1):
            print(" %d" %num, end = '  ')
        num = num  + 1
        
is_prime()






