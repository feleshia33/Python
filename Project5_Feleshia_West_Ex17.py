#Exercise #17: Prime Numbers

def is_prime():
    #input num
    num = int(input("Enter a number: "))
    #loop from 2 to num
    for prime in range(2, num):
        #return true or false
        if num % prime  == 0:
            print("False")
            break
    else:
        print("True")
is_prime()
