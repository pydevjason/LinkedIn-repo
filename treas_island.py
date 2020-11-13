def treas_island():
    looking_for_treasure = True
    while looking_for_treasure:
        print("Welcome to Treasure Island.")
        print("Your mission is to find the treasure.") 
    
        user = input("There's a fork in the road, go left or right? ").lower()
        if user == "right":
            print("wrong move!, Game over!")
            play_again = input("would you like to play again (y/n)? ").lower()
            if play_again == "y":
                continue
            else:
                looking_for_treasure = False
        elif user == "left":
            user = input("You've run into a pond, swim or wait? ").lower()
            if user == "swim":
                print("you've just been killed by a trout!, Game over.")
                play_again = input("would you like to play again (y/n)? ").lower()
                if play_again == "y":
                    continue
                else:
                    looking_for_treasure = False
            elif user == "wait":
                print("waiting.... ")
                user = input("You see a red, blue, and yellow door, which one do you enter? ").lower()
                doors = ["red", "yellow", "blue"]
                if user == doors[0]:
                    print("you've been set on fire!, game over!")
                    play_again = input("would you like to play again (y/n)? ").lower()
                    if play_again == "y":
                        continue
                    else:
                        looking_for_treasure = False
                elif user == doors[1]:
                    print("YOU WIN")
                    print("but WTH, there's no treasure!  All lies!!")
                    looking_for_treasure = False
                elif user == doors[2]:
                    print("the wild beasts just ate you!, game over!")
                    play_again = input("would you like to play again (y/n)?").lower()
                    if play_again == "y":
                        continue
                    else:
                        looking_for_treasure = False
                else:
                    print("that's a 404, game over!")
                    looking_for_treasure = False
            else:
                print("invalid input, Aw snap :( game over!")
                looking_for_treasure = False
        else:
            print("invalid input, you broke the machine, game over!")
            looking_for_treasure = False

treas_island()
