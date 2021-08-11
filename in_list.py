# This program demostrates the in operator used with a list

def main():
    # Create a list of product numbers
    prod_num = ["V234", "F345", "Q457", "E345"]

    # Get a product number to search for
    search = input("Enter a product number: ").upper()   
 
    # Determine whether the product number is in the list
    if search in prod_num:
        print(search, "was found in the list")
    else:
        print(search, "was not found in the list")

    # Call the main function
main()
