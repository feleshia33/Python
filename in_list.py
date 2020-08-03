def main():
    prod_nums = ["V475", "F345", "R345", "P234"]

    search = input("Enter a product number: ")

    if search in prod_nums:
        print(search, "was found in the list")
    else:
        print(search, "was not found in the list")

main()
