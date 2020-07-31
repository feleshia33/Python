#Exercise 4: Item Counter


def main():
    #open file
    names = open("names.txt", "r")
    #read first name in file
    name = names.readline()
    #accumlator 
    count = 0
    #loop through names in file and adds to count
    while name != "":
        count += 1
        name = names.readline()
    #close file
    names.close()    
    #print
    print ("Number of names:", count)
main()
    
