#Exercise 1: File Display

def main():
    
    #open file
    infile = open("numbers.txt", "r")
    #read file
    file_contents = infile.read()
    #close file
    infile.close()
    #print file
    print(file_contents)

main()
