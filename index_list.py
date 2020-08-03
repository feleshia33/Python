def main():
    #create food list
    food = ["Pizza", "Burgers", "Chips"]

    #display list
    print("Here is the list of food items:")
    print(food)

    #items you want to change
    item = input("Which item should I change? ")

    try:
        #gets the item's index in the list
        item_index = food.index(item)

        #get the value to replace it with
        new_item = input("Enter the new item: ")

        #replace old item with new item
        food[item_index] = new_item

        #display the list
        print("Here is the revised list:")
        print(food)

    except ValueError:
        print("That item was not found in the list")
main()
