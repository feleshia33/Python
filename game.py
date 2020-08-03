print("Welcome to my first game!")

#get name
name = input("What is your name? ")
#get age
age = int(input("What is your age? "))
print("Welcome,", name, end="")
print("!")

#number of lives
lives = 15
#age requirement
if age >= 18:
    print("You are old enough to play.")
    #want to play?
    wants_to_play = input("Do you want to play? (yes/no) " )
    if wants_to_play == "yes" or wants_to_play =="Yes" or wants_to_play == "Y":
        print("Let's play!")
        print("You are starting with", lives, "lives")
        #choice one
        left_or_right = input("First choice..left or right? (left/right) ")
        if left_or_right == "left":
                #choice two
                ans = input("Nice, you follow the path and reach a lake.."
                "do you want to swim across or go around? (across/around) ")
                if ans == "around":
                    print("You went around and reached the other side of the lake.")
                elif ans =="across":
                    print("You managed to get across, but were bit by a fish and lost"
                " 5 lives.")
                    lives -=5
                #choice three    
                ans = input("You notice a house and a river. Which do you go to (river/house)? ")
                if ans == "house":
                    print("You go to the house and is greeted by the owner..He doesn't like you and "
                          "you lose 5 lives.")
                    lives -=5
                    woods_or_trail = input("You leave the house and see the woods and trail Which do you "
                                           "choose? (woods/trail) ")
                    #choice four
                    if woods_or_trail == "trail":    
                        print("You follow the trail and reach a rainbow")
                    else:
                        print("You went into the woods and is lost forever.")
                        lives -=5
                    #lives count    
                    if lives <=0:
                            print("You now have", lives, "lives and you lost the game..")
                    else:
                            print("You have survived..and are now trillionare!")
                else:
                    print("You fell in the river and lost")      
        else:
            print("You fell down and lost..")
    else:
        print("Okay --maybe later, good-bye")
else:
    print("You are not old enough to play...")
    

