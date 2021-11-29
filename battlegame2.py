while True:

    # Declare character variables
    wizard = "Wizard"
    elf = "Elf"
    human = "Human"

    # Declare hitpoints
    wizard_hp = 70
    elf_hp = 100
    human_hp = 150

    # Declare damage
    wizard_damage = 150
    elf_damage = 100
    human_damage = 20

    # Declare dragon hitpoints and damage
    dragon_hp = 300
    dragon_damage = 50

    # List and choose character
    print("")
    print("1. Wizard")
    print("2. Elf")
    print("3. Human")
    print("")
    character = input("Select a character: ")
    character.lower()
    print("")
    
    # Determine character, hp and damage
    if character == "1" or character == "wizard" or character == "Wizard":
        print("You chosen the character:", wizard)
        character = "Wizard"
        my_hp = wizard_hp
        my_damage = wizard_damage
        print("Health:", my_hp)
        print("Damage:", my_damage)
        print("")
        break
    elif character == "2" or character == "elf" or character == "Elf":
        print("You chosen the character:", elf)
        character = "Elf"
        my_hp = elf_hp
        my_damage = elf_damage
        print("Health:", my_hp)
        print("Damage:", my_damage)
        print("")
        break
    elif character == "3" or character == "human" or character == "Human":
        print("You chosen the charcter:", human)
        character = "Human"
        print("")
        my_hp = human_hp
        my_damage = human_damage
        print("Health:", my_hp)
        print("Damage:", my_damage)
        print("")
        break
    else: 
        print("Character unknown, try again")
        print("")
        continue

while True:
    # Character strikes Dragon
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damage the Dragon!")
    print("The Dragon's hitpoints are now:", dragon_hp)
    print("")
    if dragon_hp <= 0: 
        print("The Dragon has lost the battle")
        print("")
        break
    # Dragon strikes Character
    print("The Dragon strikes back at the ", character)
    my_hp = my_hp - dragon_damage
    print("The", character, "hitpoints are now", my_hp)
    print("")
    if my_hp <= 0:
        print("The", character, "has lost the battle")
        print("")
        break

   






