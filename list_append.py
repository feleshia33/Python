def main():
    #create empty list
    name_list = []

    #control loop variable
    again = 'y'

    #add names to list
    while again == 'y':
        name = input("Enter a name: ")

        #append name to list
        name_list.append(name)
        #add another name
        print("Do you want to add another name? ")
        again = input("y = yes, anything else = no: ")
        print()
    #print names
    print("Here are the names you entered: ")
    print()
    #prints name
    for name in name_list:
        print(name)

main()
