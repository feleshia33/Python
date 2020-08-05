def main():
    food = ["pizza", "burgers", "tacos"]

    print('Here are the items in the food list')
    print(food)

    item = input("Which item should I remove? ")

    try:
        food.remove(item)

        print("Here is the new list of food items")
        print(food)


    except ValueError:
        print("That item was not in the list.")

main()
