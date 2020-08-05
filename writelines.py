#this program uses the writelines method to save a list of strings in a file.

def main():
    
    cities = ["Austin", "Boston", "Dallas"]

    outfile = open("cities.txt", "w")

    for item in cities:
        outfile.write(item + "\n")

    outfile.close()

main()
